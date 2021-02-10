<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
import logging
=======
import logging

>>>>>>> 33f1bd1 (ECC - 420 Implemented validation on request data & sending response accordingly)
from rest_framework.utils import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers import MetadataLedgerSerializer

logger = logging.getLogger('dict_config_logger')


class MetadataLedgerView(APIView):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 33f1bd1 (ECC - 420 Implemented validation on request data & sending response accordingly)
    """
    List all snippets, or create a new snippet.
    """
    # def get(self, request, format=None):
    #     metadata_ledger = MetadataLedger.objects.all()
    #     serializer = MetadataLedgerSerializer(metadata_ledger, many=True)
    #     return Response(serializer.data)
<<<<<<< HEAD
=======
    """Receive metadata_ledger data from XIA"""
>>>>>>> 0d964ae (ECC-420 Validation of metadata in XIS request)
=======
>>>>>>> 33f1bd1 (ECC - 420 Implemented validation on request data & sending response accordingly)
=======
    """Receive metadata_ledger data from XIA"""
>>>>>>> 0d964ae (ECC-420 Validation of metadata in XIS request)

    def post(self, request):
        serializer = MetadataLedgerSerializer(data=request.data)
        logger.info("Assigned to serializer")

        if serializer.is_valid():
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 0d964ae (ECC-420 Validation of metadata in XIS request)
            # If received save record in ledger and send response of UUID &
            # created status
            logger.info(json.dumps(request.data))
            serializer.save()
            return Response(serializer.data['unique_record_identifier'],
                            status=status.HTTP_201_CREATED)
        else:
            # If not received send error and bad request status
            logger.info(json.dumps(request.data))
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
=======
from django.shortcuts import render
=======
>>>>>>> 7d29966 (fixed flake8 warnings)
=======
import logging

from rest_framework.utils import json
>>>>>>> d4f8b38 (Adding XIA to XIS metadata_ledger using REST_API.)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import MetadataLedger
from api.serializers import MetadataLedgerSerializer
=======
from django.shortcuts import render
=======
>>>>>>> 7d29966 (fixed flake8 warnings)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api import serializers
import logging
import json
<<<<<<< HEAD

<<<<<<< HEAD
>>>>>>> 21f2f28 (added new core app; fixed secret key docker config)

=======
>>>>>>> 6ee8a72 (Add draft of views.py)
=======
from api.serializers import MetadataLedgerSerializer, SupplementalLedgerSerializer
>>>>>>> 8b66375 (Made corrections to serializers.py and views.py.)
logger = logging.getLogger('dict_config_logger')

class MetadataLedgerView(APIView):
<<<<<<< HEAD
=======
import logging
from rest_framework.utils import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import MetadataLedger
from api.serializers import MetadataLedgerSerializer

logger = logging.getLogger('dict_config_logger')

class MetadataLedgerView(APIView):
>>>>>>> d4f8b38 (Adding XIA to XIS metadata_ledger using REST_API.)
    """
    List all snippets, or create a new snippet.
    """
    # def get(self, request, format=None):
    #     metadata_ledger = MetadataLedger.objects.all()
    #     serializer = MetadataLedgerSerializer(metadata_ledger, many=True)
    #     return Response(serializer.data)

    def post(self, request, format=None):
<<<<<<< HEAD
<<<<<<< HEAD
        serializer = MetadataLedgerSerializer(data=request.data)
        if serializer.is_valid():
            logger.info(json.dumps(request.data))
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            logger.info(json.dumps(request.data))
<<<<<<< HEAD
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
<<<<<<< HEAD
            )
<<<<<<< HEAD

        
>>>>>>> 21f2f28 (added new core app; fixed secret key docker config)
=======
>>>>>>> 7d29966 (fixed flake8 warnings)
=======
            )
>>>>>>> 8b66375 (Made corrections to serializers.py and views.py.)
=======
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

>>>>>>> d4f8b38 (Adding XIA to XIS metadata_ledger using REST_API.)
=======
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
>>>>>>> 0f26a51 (Minor changes to models.py and serializers.py)
=======
            logger.info(json.dumps(request.data))
            serializer.save()
            return Response(serializer.data['unique_record_identifier'], status=status.HTTP_201_CREATED)
        else:
            logger.info(json.dumps(request.data))
<<<<<<< HEAD


            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST



            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
>>>>>>> 33f1bd1 (ECC - 420 Implemented validation on request data & sending response accordingly)
=======
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
>>>>>>> aaa8cae (Commits before rebase)
=======
    """Test API VIew"""
    metadataSerializer_class = serializers.MetadataLedgerSerializer
    supplementSerializer_class = serializers.SupplementalLedgerSerializer
    def post(self, request):
        """Takes in a JSON object and prints to the console"""
        metadataSerializer = self.metadataSerializer_class(data=request.data)
        #supplementalSerializer = self.supplementSerializer_class(data=request.data)
        # Check if metadataSerializer is valid AND supplementalSerializer is
        # valid
<<<<<<< HEAD
=======
        serializer = MetadataLedgerSerializer(data=request.data, many= True)
>>>>>>> d4f8b38 (Adding XIA to XIS metadata_ledger using REST_API.)
=======
        serializer = MetadataLedgerSerializer(data=request.data)
>>>>>>> a9a1ac2 (Adding Views.py for accepting a json record over REST API functionality)
        if serializer.is_valid():
            logger.info(json.dumps(request.data))
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            logger.info(json.dumps(request.data))
<<<<<<< HEAD
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
<<<<<<< HEAD
            )
<<<<<<< HEAD

        
>>>>>>> 21f2f28 (added new core app; fixed secret key docker config)
=======
>>>>>>> 7d29966 (fixed flake8 warnings)
=======
            )
>>>>>>> 8b66375 (Made corrections to serializers.py and views.py.)
=======
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

>>>>>>> d4f8b38 (Adding XIA to XIS metadata_ledger using REST_API.)
=======
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
>>>>>>> 0f26a51 (Minor changes to models.py and serializers.py)
