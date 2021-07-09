import logging

from celery.result import AsyncResult
from django.http import HttpResponse, JsonResponse
from requests.exceptions import HTTPError
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.utils import json

from api.serializers import CompositeLedgerSerializer, MetadataLedgerSerializer
from core.models import CompositeLedger, MetadataLedger
from core.tasks import xis_workflow

logger = logging.getLogger('dict_config_logger')


def get_course_providers(request):
    """This method defines an API to fetch the names of all course providers"""
    providers = list(CompositeLedger.objects.order_by()
                     .values_list('provider_name', flat=True).distinct())
    result = json.dumps(providers)

    return HttpResponse(result, content_type="application/json")


@api_view(['GET', 'POST'])
def metadata_list(request):
    """Handles creating metadata record and listing composite ledger records"""
    if request.method == 'GET':
        errorMsg = {
            "message": "Error fetching records please check the logs."
        }
        # initially fetch all active records
        querySet = CompositeLedger.objects.all().order_by()\
            .filter(record_status='Active')

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
                    "message": "Error; no unique record identidier found for: "
                    + id_param
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

    elif request.method == 'POST':
        # Obtaining key value for comparison of records in metadata ledger
        key_hash_value = request.data.get('metadata_key_hash', None)
        record_in_table = None
        if key_hash_value is not None:
            # Comparing metadata_key value in metadata ledger
            # to find older instances
            record_in_table = MetadataLedger.objects.filter(
                metadata_key_hash=key_hash_value, record_status='Active') \
                .first()

        # Assign data from request to serializer
        serializer = MetadataLedgerSerializer(record_in_table,
                                              data=request.data)
        logger.info("Assigned to serializer")

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


@api_view(['GET'])
def record_for_requested_course_id(request, course_id):
    """This method defines an API to fetch the record of the
    corresponding course id"""
    errorMsg = {
        "message": "error: no record for corresponding course id; " +
                   "please check the logs"
    }

    try:
        queryset = CompositeLedger.objects.order_by() \
            .get(unique_record_identifier=course_id, record_status='Active')
        serializer_class = CompositeLedgerSerializer(queryset)
    except HTTPError as http_err:
        logger.error(http_err)
        return Response(errorMsg, status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as err:
        logger.error(err)
        return Response(errorMsg, status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response(serializer_class.data, status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def xis_workflow_api(request):
    print('XIS workflow api')
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
