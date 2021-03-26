import logging

from rest_framework import status
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

from api.serializers import MetadataLedgerSerializer
from core.models import MetadataLedger

logger = logging.getLogger('dict_config_logger')


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
                metadata_key_hash=key_hash_value, record_status='Active')\
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
