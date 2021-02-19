from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api import serializers
import logging
import json
from api.serializers import MetadataLedgerSerializer, SupplementalLedgerSerializer
logger = logging.getLogger('dict_config_logger')

class MetadataLedgerView(APIView):
    """Test API VIew"""
    metadataSerializer_class = serializers.MetadataLedgerSerializer
    supplementSerializer_class = serializers.SupplementalLedgerSerializer
    def post(self, request):
        """Takes in a JSON object and prints to the console"""
        metadataSerializer = self.metadataSerializer_class(data=request.data)
        #supplementalSerializer = self.supplementSerializer_class(data=request.data)
        # Check if metadataSerializer is valid AND supplementalSerializer is
        # valid
        if metadataSerializer.is_valid():
            unique_record_identifier = metadataSerializer.validated_data.get('unique_record_identifier')
            agent_name = metadataSerializer.validated_data.get('agent_name')
            date_inserted = metadataSerializer.validated_data.get('date_inserted')
            metadata_key = metadataSerializer.validated_data.get('metadata_key')
            metadata_hash = metadataSerializer.validated_data.get('metadata_hash')
            metadata = metadataSerializer.validated_data.get('metadata')
            record_status = metadataSerializer.validated_data.get('record_status')
            date_deleted = metadataSerializer.validated_data.get('date_deleted')
            metadata_validation_date = metadataSerializer.validated_data.get('metadata_validation_date')
            metadata_validation_status = metadataSerializer.validated_data.get('metadata_validation_status')
            logger.info(json.dumps(request.data))
            return Response(metadataSerializer)
        else:
            logger.info(json.dumps(request_data))
            return Response(
                metadataSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
            # convert both serializers into 1 JSON object, and return it in
            # the response