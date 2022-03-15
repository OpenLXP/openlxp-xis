import logging
import uuid

from celery.result import AsyncResult
from django.http import JsonResponse
# from core.management.commands.load_metadata_into_neo4j import \
#     Command as load_metadata_into_neo4j
from requests.exceptions import HTTPError
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

from api.management.utils.api_helper_functions import (add_metadata_ledger,
                                                       add_supplemental_ledger)
from api.serializers import CompositeLedgerSerializer, \
    MetadataLedgerSerializer, SupplementalLedgerSerializer
from core.management.utils.transform_ledgers import (
    append_metadata_ledger_with_supplemental_ledger,
    detach_metadata_ledger_from_supplemental_ledger)
from core.models import CompositeLedger, MetadataLedger
from core.tasks import xis_workflow

logger = logging.getLogger('dict_config_logger')


class CatalogDataView(APIView):
    """Handles HTTP requests for Provider data from XIS"""

    def get(self, request):
        """This method defines an API to fetch the names of all
         course providers"""
        errorMsg = {
            "message": "Error fetching records please check the logs."
        }
        try:
            providers = list(CompositeLedger.objects.
                             order_by().values_list('provider_name',
                                                    flat=True).distinct())

            if not providers:
                errorMsg = {
                    "message": "No catalogs present in records"
                }
                return Response(errorMsg, status.HTTP_404_NOT_FOUND)

            result = json.dumps(providers)

        except HTTPError as http_err:
            logger.error(http_err)
            return Response(errorMsg,
                            status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as err:
            logger.error(err)
            return Response(errorMsg, status.HTTP_404_NOT_FOUND)
        else:
            return Response(result, status.HTTP_200_OK)


class ManagedCatalogListView(APIView):
    """Handles HTTP requests for Provider data from XIS"""

    def get(self, request):
        """This method defines an API to fetch the names of all
         course providers"""
        errorMsg = {
            "message": "Error fetching records please check the logs."
        }
        try:
            providers = list(MetadataLedger.objects.
                             order_by().values_list('provider_name',
                                                    flat=True).distinct())

            if not providers:
                errorMsg = {
                    "message": "No catalogs present in records"
                }
                return Response(errorMsg, status.HTTP_404_NOT_FOUND)

            result = json.dumps(providers)

        except HTTPError as http_err:
            logger.error(http_err)
            return Response(errorMsg,
                            status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as err:
            logger.error(err)
            return Response(errorMsg, status.HTTP_404_NOT_FOUND)
        else:
            return Response(result, status.HTTP_200_OK)


class MetaDataView(APIView):
    """Handles HTTP requests for Metadata for XIS"""

    def get(self, request):
        """This method defines the API's to retrieve data from
        composite ledger from XIS"""

        errorMsg = {
            "message": "Error fetching records please check the logs."
        }
        # initially fetch all active records
        querySet = CompositeLedger.objects.all().order_by() \
            .filter(record_status='Active')

        if not querySet:
            errorMsg = {
                "message": "Error no records found"
            }

            return Response(errorMsg, status.HTTP_400_BAD_REQUEST)

        # case where provider sent as query parameter
        if request.GET.get('provider'):
            querySet = querySet.filter(provider_name=request.GET.
                                       get('provider'))

            if not querySet:
                errorMsg = {
                    "message": "Error; no provider name found for: " +
                               request.GET.get('provider')
                }

                return Response(errorMsg, status.HTTP_400_BAD_REQUEST)
        # case a list of ids sent as query parameter e.g a,b,c,d
        elif request.GET.get('id'):
            id_param = request.GET.get('id')
            ids = id_param.split(",")
            querySet = querySet.filter(unique_record_identifier__in=ids)

            if not querySet:
                errorMsg = {
                    "message": "Error; no unique record identifier found for: "
                               + id_param
                }

                return Response(errorMsg, status.HTTP_400_BAD_REQUEST)

        # case where a list of metadata key hashes is sent as query parameter
        # e.g a,b,c
        if request.GET.get('metadata_key_hash_list'):
            metadata_key_hash_param = request.GET.get('metadata_key_hash_list')
            hashes = metadata_key_hash_param.split(',')
            querySet = querySet.filter(metadata_key_hash__in=hashes)

            if not querySet:
                errorMsg = {
                    "message": "Error; no record found for any of the "
                               + "following key hashes: " +
                               metadata_key_hash_param
                }

                return Response(errorMsg, status.HTTP_400_BAD_REQUEST)

        try:
            serializer_class = CompositeLedgerSerializer(querySet, many=True)
        except HTTPError as http_err:
            logger.error(http_err)
            return Response(errorMsg, status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as err:
            logger.error(err)
            return Response(errorMsg, status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer_class.data, status.HTTP_200_OK)

    def post(self, request):
        """This method defines the API's to save data to the
        metadata ledger in the XIS"""

        # Tracking source of changes to metadata/supplementary data
        request.data['updated_by'] = "System"
        data, instance = add_metadata_ledger(request.data, None)
        serializer = \
            MetadataLedgerSerializer(instance, data=data)

        if not serializer.is_valid():
            # If not received send error and bad request status
            logger.info(json.dumps(request.data))
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        # If received save record in ledger and send response of UUID &
        # status created
        serializer.save()

        return Response(serializer.data['unique_record_identifier'],
                        status=status.HTTP_201_CREATED)


class SupplementalDataView(APIView):
    """Handles HTTP requests for Supplemental data for XIS"""

    def post(self, request):
        """This method defines the API's to save data to the
        metadata ledger in the XIS"""

        # Tracking source of changes to metadata/supplementary data
        request.data['updated_by'] = 'System'

        data, instance = add_supplemental_ledger(request.data, None)

        serializer = \
            SupplementalLedgerSerializer(instance,
                                         data=data)

        if not serializer.is_valid():
            # If not received send error and bad request status
            logger.info(json.dumps(request.data))
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

        # If received save record in ledger and send response of UUID &
        # status created
        serializer.save()
        return Response(serializer.data['unique_record_identifier'],
                        status=status.HTTP_201_CREATED)


class UUIDDataView(APIView):
    """Handles HTTP requests using UUID from composite ledger"""

    def get(self, request, course_id):
        """This method defines an API to fetch or modify the record of the
        corresponding course id"""
        errorMsg = {
            "message": "error: no record for corresponding course id; " +
                       "please check the logs"
        }
        try:
            queryset = CompositeLedger.objects.order_by() \
                .get(unique_record_identifier=course_id,
                     record_status='Active')
            serializer_class = CompositeLedgerSerializer(queryset)
        except HTTPError as http_err:
            logger.error(http_err)
            return Response(errorMsg, status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as err:
            logger.error(err)
            return Response(errorMsg, status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer_class.data, status.HTTP_200_OK)


class ManagedCatalogDataView(APIView):
    """Handles HTTP requests for Managing catalog data from XMS"""
    errorMsg = {
        "message": "Error fetching records please check the logs."
    }

    def get(self, request, provider_id):
        """This method defines the API's to retrieve data to be managed
         from XMS"""

        fields = ('unique_record_identifier', 'metadata_key',
                  'metadata_key_hash', 'metadata_hash', 'metadata',
                  'provider_name')

        querySet = MetadataLedger.objects.filter(
            provider_name=provider_id,
            record_status="Active"
        )

        if not querySet:
            errorMsg = {"Error; no active records found for the provider "
                        + provider_id}
            logger.error(errorMsg)
            return Response(errorMsg, status.HTTP_404_NOT_FOUND)

        try:
            serializer_data = MetadataLedgerSerializer(querySet,
                                                       many=True,
                                                       fields=fields).data
            transformed_metadata = \
                append_metadata_ledger_with_supplemental_ledger(
                    serializer_data[0])[0]
            serializer_data[0]['metadata'] = transformed_metadata

        except HTTPError as http_err:
            logger.error(http_err)
            return Response(self.errorMsg,
                            status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as err:
            logger.error(err)
            return Response(self.errorMsg,
                            status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer_data, status.HTTP_200_OK)


class ManageDataView(APIView):
    """Handles HTTP requests for Managing data from XMS"""
    errorMsg = {
        "message": "Error fetching records please check the logs."
    }

    def get(self, request, provider_id, experience_id):
        """This method defines the API's to retrieve data to be managed
         from XMS"""

        fields = ('unique_record_identifier', 'metadata_key',
                  'metadata_key_hash', 'metadata_hash', 'metadata',
                  'provider_name')

        querySet = MetadataLedger.objects.filter(
            metadata_key_hash=experience_id,
            provider_name=provider_id,
            record_status="Active"
        )

        if not querySet:
            errorMsg = {"Error; no active records found for metadata key " +
                        experience_id + " in provider " + provider_id}
            logger.error(errorMsg)

            return Response(errorMsg, status.HTTP_404_NOT_FOUND)

        try:
            serializer_data = MetadataLedgerSerializer(querySet,
                                                       many=True,
                                                       fields=fields).data
            transformed_metadata = \
                append_metadata_ledger_with_supplemental_ledger(
                    serializer_data[0])[0]
            serializer_data[0]['metadata'] = transformed_metadata

        except HTTPError as http_err:
            logger.error(http_err)
            return Response(self.errorMsg,
                            status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as err:
            logger.error(err)
            return Response(self.errorMsg,
                            status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer_data, status.HTTP_200_OK)

    def post(self, request, provider_id, experience_id):
        """This method defines the API's to save data
        after it's been managed in XMS"""

        # Tracking source of changes to metadata/supplementary data
        request.data['updated_by'] = "Owner"
        request.data['provider_name'] = provider_id
        request.data['metadata_key_hash'] = experience_id
        request.data['unique_record_identifier'] = str(uuid.uuid4())

        # Detach supplemental metadata and metadata from consolidated data
        metadata_data, supplemental_data = \
            detach_metadata_ledger_from_supplemental_ledger(request.data)

        metadata, metadata_instance = add_metadata_ledger(metadata_data,
                                                          experience_id)

        supplementalData, supplemental_instance = \
            add_supplemental_ledger(supplemental_data, experience_id)

        if metadata_instance:

            metadata['metadata_key'] = metadata_instance.metadata_key

            # Assign data from request to serializer
            metadata_serializer = MetadataLedgerSerializer(metadata_instance,
                                                           data=metadata)

            # Assign data from request to serializer
            supplemental_serializer = \
                SupplementalLedgerSerializer(supplemental_instance,
                                             data=supplementalData)

            if not metadata_serializer.is_valid():
                # If not received send error and bad request status
                logger.info(json.dumps(metadata_data))
                logger.error(metadata_serializer.errors)
                return Response(metadata_serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)

            if not supplemental_serializer.is_valid():
                # If not received send error and bad request status
                logger.info(json.dumps(supplemental_data))
                logger.error(supplemental_serializer.errors)
                return Response(supplemental_serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)

            # If received save record in ledger and send response of UUID &
            # status created
            metadata_serializer.save()
            supplemental_serializer.save()

            return Response(metadata_serializer.data['metadata_key_hash'],
                            status=status.HTTP_201_CREATED)
        else:
            errorMsg = {
                "message": "Course updated does not exist in records. Please "
                           "check experience value"
            }
            return Response(errorMsg, status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def xis_workflow_api(request):
    logger.info('XIS workflow api')
    task = xis_workflow.delay()
    return JsonResponse({"task_id": task.id}, status=202)


def get_status(request, task_id):
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result
    }
    return JsonResponse(result, status=200)

# @api_view(['GET'])
# def post_to_neo4j(request):
#     """ API which post metadata from Composite_Ledger XIS to Neo4j Graph
#     Database"""
#     load_metadata_into_neo4j_class = load_metadata_into_neo4j()
#
#     function = load_metadata_into_neo4j_class.handle()
#     function.delay()
#     return Response('ok', status=200)
