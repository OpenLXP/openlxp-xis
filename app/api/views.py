from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api import serializers

import logging
import sys
import json


logger = logging.getLogger('dict_config_logger')

class MetadataLedgerView(APIView):
    """Test API VIew"""
    serializer_class = serializers.TestObjectSerializer
    # metadataSerializer_class = serializers.[serializer_name]
    # supplementSerializer_class = serializers.[serializer_name]

    def post(self, request):
        """Takes in a JSON object and prints to the console"""
        
        serializer = self.serializer_class(data=request.data)
        #metadataJSON = 
        # supplementalJSON = 
        # metadataSerializer = self.metadataSerializer_class(metadataJSON)
        # supplementalSerializer = 
            #  self.supplementSerializer_class(supplementalJSON)

        # Check if metadataSerializer is valid AND supplementalSerializer is
            # valid
        if serializer.is_valid():
            # name = serializer.validated_data.get('name')
            # age = serializer.validated_data.get('age')
            # occupation = serializer.validated_data.get('occupation')
            logger.info(json.dumps(request.data))

            # convert both serializers into 1 JSON object, and return it in
            # the response
            return Response(serializer)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        