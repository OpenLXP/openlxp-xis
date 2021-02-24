import logging

from rest_framework.utils import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers import MetadataLedgerSerializer

logger = logging.getLogger('dict_config_logger')


class MetadataLedgerView(APIView):
    """Receive metadata_ledger data from XIA"""

    def post(self, request):
        serializer = MetadataLedgerSerializer(data=request.data)
        logger.info("Assigned to serializer")

        if serializer.is_valid():
            # If received save record in ledger and send response of UUID &
            # created status
            logger.info(json.dumps(request.data))
            serializer.save()
            return Response(serializer.data['unique_record_identifier'], status=status.HTTP_201_CREATED)
        else:
            # If not received send error and bad request status
            logger.info(json.dumps(request.data))
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
