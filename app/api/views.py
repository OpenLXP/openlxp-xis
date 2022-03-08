import hashlib
import logging

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

from api.serializers import (CompositeLedgerSerializer,
                             MetadataLedgerSerializer,
                             SupplementalLedgerSerializer)
from core.management.utils.transform_ledgers import (
    append_metadata_ledger_with_supplemental_ledger,
    detach_metadata_ledger_from_supplemental_ledger)
from core.models import CompositeLedger, MetadataLedger, SupplementalLedger
from core.tasks import xis_workflow

logger = logging.getLogger('dict_config_logger')


def add_metadata_ledger(data):
    """Calls the metadata serializer with data sent over
     and older instance of the data """
    # Obtaining key value for comparison of records in metadata ledger
    key_hash_value = data.get('metadata_key_hash', None)
    record_in_table = None
    if key_hash_value is not None:
        # Comparing metadata_key value in metadata ledger
        # to find older instances
        record_in_table = MetadataLedger.objects.filter(
            metadata_key_hash=key_hash_value, record_status='Active') \
            .first()

    # Assign data from request to serializer
    serializer = MetadataLedgerSerializer(record_in_table,
                                          data=data)
    return serializer


def add_supplemental_ledger(data):
    """Calls the supplemental serializer with data sent over
         and older instance of the data """
    # Obtaining key value for comparison of records in metadata ledger
    key_hash_value = data.get('metadata_key_hash', None)
    record_in_table = None
    if key_hash_value is not None:
        # Comparing key value in metadata ledger
        # to find older instances
        record_in_table = SupplementalLedger.objects.filter(
            metadata_key_hash=key_hash_value, record_status='Active') \
            .first()

    # Assign data from request to serializer
    serializer = SupplementalLedgerSerializer(record_in_table,
                                              data=data)

    return serializer


class CatalogDataView(APIView):
    """Handles HTTP requests for Provider data from XIS"""

    def get(self, request):
        """This method defines an API to fetch the names of all
         course providers"""
        errorMsg = {
            "message": "Error fetching records please check the logs."
        }

        providers = list(CompositeLedger.objects.order_by().
                         values_list('provider_name', flat=True).distinct())
        result = json.dumps(providers)

        try:
            if not bool(providers):
                raise ValueError
        except HTTPError as http_err:
            logger.error(http_err)
            return Response(errorMsg,
                            status.HTTP_500_INTERNAL_SERVER_ERROR)
        except ValueError:
            errorMsg = {
                "message": "No catalogs present"
            }
            logger.error(errorMsg)
            return Response(errorMsg, status.HTTP_400_BAD_REQUEST)
        else:
            return Response(result, status.HTTP_200_OK)


class ProviderDataView(APIView):
    """Handles HTTP requests for Provider data from XIS"""

    def get(self, request):
        """This method defines an API to fetch the names of all
         course providers"""
        errorMsg = {
            "message": "Error fetching records please check the logs."
        }

        providers = list(MetadataLedger.objects.order_by()
                         .values_list('provider_name', flat=True).distinct())
        result = json.dumps(providers)

        try:
            if not bool(providers):
                raise ValueError
        except HTTPError as http_err:
            logger.error(http_err)
            return Response(errorMsg,
                            status.HTTP_500_INTERNAL_SERVER_ERROR)
        except ValueError:
            errorMsg = {
                "message": "No catalogs present"
            }
            logger.error(errorMsg)
            return Response(errorMsg, status.HTTP_400_BAD_REQUEST)
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
        if request.GET.get('metadata_key_hash'):
            metadata_key_hash_param = request.GET.get('metadata_key_hash')
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
        serializer = add_metadata_ledger(request.data)

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

        serializer = add_supplemental_ledger(request.data)

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


class ManageDataView(APIView):
    """Handles HTTP requests for Managing data from XMS"""
    errorMsg = {
        "message": "Error fetching records please check the logs."
    }

    def get(self, request):
        """This method defines the API's to retrieve data to be managed
         from XMS"""

        course_key = request.GET.get('metadata_key_hash', None)

        # case where metadata key hashes are sent as query parameter

        fields = ('unique_record_identifier', 'metadata_key',
                  'metadata_key_hash', 'metadata_hash', 'metadata',
                  'provider_name', 'metadata_validation_status',
                  'record_status', 'updated_by')

        Managed_metadata = MetadataLedger.objects. \
            filter(metadata_key_hash=course_key,
                   metadata_validation_status='Y',
                   record_status='Active')

        if not Managed_metadata:
            errorMsg = {
                "message": "Error; no record found for the "
                           + "following key hash: " +
                           course_key
            }

            return Response(errorMsg, status.HTTP_400_BAD_REQUEST)

        try:
            serializer_data = MetadataLedgerSerializer(Managed_metadata,
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

    def post(self, request):
        """This method defines the API's to save data
        after it's been managed in XMS"""

        # Tracking source of changes to metadata/supplementary data
        request.data['updated_by'] = "Owner"

        # Detach supplemental metadata and metadata from consolidated data
        metadata_data, supplemental_data = \
            detach_metadata_ledger_from_supplemental_ledger(request.data)

        # create hash values of metadata and supplemental data
        metadata_hash = hashlib.sha512(str(metadata_data['metadata']).encode(
            'utf-8')).hexdigest()
        supplemental_hash = hashlib.sha512(str(supplemental_data['metadata'])
                                           .encode('utf-8')).hexdigest()

        # assign hash values to hash key in data
        metadata_data['metadata_hash'] = metadata_hash
        supplemental_data['metadata_hash'] = supplemental_hash

        metadata_serializer = add_metadata_ledger(metadata_data)
        supplemental_serializer = add_supplemental_ledger(supplemental_data)

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
