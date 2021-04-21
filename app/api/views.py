import logging

from rest_framework import status
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView
from django.http import (HttpResponse, HttpResponseBadRequest,
                         HttpResponseServerError)
from requests.exceptions import HTTPError

from api.serializers import MetadataLedgerSerializer, CompositeLedgerSerializer
from core.models import MetadataLedger, CompositeLedger

logger = logging.getLogger('dict_config_logger')


def get_course_providers(request):
    """This method defines an API to fetch the names of all course providers"""
    providers = list(CompositeLedger.objects.order_by() \
                     .values_list('provider_name').distinct())
    result = json.dumps(providers)

    return HttpResponse(result, content_type="application/json")


def records_for_provider_name(request, provider):
    """This method defines an API to fetch the record of the
    corresponding course providers"""
    results = []

    errorMsg = {
        "message": "error: no record for corresponding provider name; " +
                   "please check the logs"
    }
    errorMsgJSON = json.dumps(errorMsg)
    try:
        queryset = CompositeLedger.objects.all().order_by(). \
            filter(provider_name=provider)
        serializer_class = CompositeLedgerSerializer(queryset, many=True)
    except HTTPError as http_err:
        logger.error(http_err)
        return HttpResponseServerError(errorMsgJSON,
                                       content_type="application/json")
    except Exception as err:
        logger.error(err)
        return HttpResponseServerError(errorMsgJSON,
                                       content_type="application/json")
    else:
        logger.info(queryset)
        return HttpResponse(serializer_class.data, content_type="application/json")

    # try:
    #     response = more_like_this(doc_id=doc_id)
    #     results = get_results(response)
    # except HTTPError as http_err:
    #     logger.error(http_err)
    #     return HttpResponseServerError(errorMsgJSON,
    #                                    content_type="application/json")
    # except Exception as err:
    #     logger.error(err)
    #     return HttpResponseServerError(errorMsgJSON,
    #                                    content_type="application/json")
    # else:
    #     logger.info(results)
    #     return HttpResponse(results, content_type="application/json")


class MetadataLedgerView(APIView):
    """Receive metadata_ledger data from XIA"""

    def post(self, request):
        """POST request are handled here"""

        # obtaining key value for comparison of records in metadata ledger
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
        # created status
        serializer.save()
        return Response(serializer.data['unique_record_identifier'],
                        status=status.HTTP_201_CREATED)
