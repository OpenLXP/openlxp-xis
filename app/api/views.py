import logging

from rest_framework.utils import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import MetadataLedger
from api.serializers import MetadataLedgerSerializer

logger = logging.getLogger('dict_config_logger')

class MetadataLedgerView(APIView):
    """
    List all snippets, or create a new snippet.
    """
    # def get(self, request, format=None):
    #     metadata_ledger = MetadataLedger.objects.all()
    #     serializer = MetadataLedgerSerializer(metadata_ledger, many=True)
    #     return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MetadataLedgerSerializer(data=request.data, many= True)
        if serializer.is_valid():
            logger.info(json.dumps(request.data))
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            logger.info(json.dumps(request.data))
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

