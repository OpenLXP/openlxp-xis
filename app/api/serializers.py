<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
from django.utils import timezone
import logging
from rest_framework import serializers
from api.models import MetadataLedger, SupplementalLedger
from core.utils.utils import \
    get_required_recommended_fields_for_target_validation
=======
from django.utils import timezone
import logging
from rest_framework import serializers
from api.models import MetadataLedger, SupplementalLedger
from core.utils.utils import \
    get_required_recommended_fields_for_target_validation

logger = logging.getLogger('dict_config_logger')

>>>>>>> 33f1bd1 (ECC - 420 Implemented validation on request data & sending response accordingly)

<<<<<<< HEAD
logger = logging.getLogger('dict_config_logger')


class MetadataLedgerSerializer(serializers.ModelSerializer):
    """Serializes an entry into the Metadata Ledger"""

    class Meta:
        model = MetadataLedger

        fields = ['unique_record_identifier',
                  'provider_name',
                  'date_inserted',
                  'metadata_key',
                  'metadata_hash',
                  'metadata',
                  'record_status',
                  'date_deleted',
                  'metadata_validation_date',
                  'metadata_validation_status']

    def validate(self, data):
        """function to validate metadata field"""

        # Call function to get required & recommended values
        required_dict, recommended_dict = \
            get_required_recommended_fields_for_target_validation()
        json_metadata = data.get('metadata')
        validation_result = 'Y'
        for column in json_metadata:
            required_columns = required_dict[column]
            recommended_columns = recommended_dict[column]
            for key in json_metadata[column]:
                if key in required_columns:
                    if not json_metadata[column][key]:
                        logger.info(
                            "Record " + str(
                                data.get('unique_record_identifier')
                            ) + "does not have all "
                                "REQUIRED "
                                "fields. " + key + "field"
                                                   " is "
                                                   " empty")
                        validation_result = 'N'
                    if key in recommended_columns:
                        if not json_metadata[column][key]:
                            logger.info(
                                "Record " + str(
                                    data.unique_record_identifier) +
                                " does not have all RECOMMENDED fields. " +
                                key + " field is empty")
            data['metadata_validation_status'] = validation_result
            data['metadata_validation_date'] = timezone.now()
        logger.info(data['metadata_validation_status'],
                    data['metadata_validation_date'])
        return data
=======
from django.utils import timezone
from rest_framework import serializers
from api.models import MetadataLedger
>>>>>>> d4f8b38 (Adding XIA to XIS metadata_ledger using REST_API.)

<<<<<<< HEAD
# class SupplementalLedgerSerializer(serializers.Serializer):
#     """Serializes an entry into the Supplemental Ledger"""
#
#     class Meta:
#         model = SupplementalLedger
#         fields = ('unique_record_identifier',
#                   'agent_name',
#                   'date_inserted',
#                   'metadata_key',
#                   'metadata_hash',
#                   'metadata',
#                   'record_status',
#                   'date_deleted',
#                   'metadata_validation_date',
#                   'metadata_validation_status')
#         extra_kwargs:{
#             'unique_record_identifier': {'max_length': 50},
#             'agent_name': {'max_length': 255},
#             'date_inserted': {'blank': True, 'null': True},
#             'metadata_hash': {'max_length': 200},
#             'metadata': {'blank': True},
#             'record_status': {'max_length': 10,
#                               'blank': True,
#                               'choices': SupplementalLedger.RECORD_ACTIVATION_STATUS_CHOICES
#                               },
#             'date_deleted': {'blank': True, 'null': True},
#             'metadata_validation_date': {'blank': True, 'null': True},
#             'metadata_validation_status': {'max_length': 10,
#                                            'blank': True,
#                                            'choices': SupplementalLedger.METADATA_VALIDATION_CHOICES}
#         }
=======
=======
from django.utils import timezone
>>>>>>> d4f8b38 (Adding XIA to XIS metadata_ledger using REST_API.)
from rest_framework import serializers
from api.models import MetadataLedger


<<<<<<< HEAD
=======
from rest_framework import serializers
from api.models import MetadataLedger, SupplementalLedger

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 21f2f28 (added new core app; fixed secret key docker config)
=======

<<<<<<< HEAD
>>>>>>> 7d29966 (fixed flake8 warnings)
class TestObjectSerializer(serializers.Serializer):
    """Serializes a sample JSON object"""
    name = serializers.CharField()
    age = serializers.IntegerField()
    occupation = serializers.CharField()

<<<<<<< HEAD
<<<<<<< HEAD
=======

# 1. MetadataLedgerSerializer
>>>>>>> 33f1bd1 (ECC - 420 Implemented validation on request data & sending response accordingly)

<<<<<<<< HEAD:app/api/serializers.py
# 2. SupplementalLedgerSerializer
<<<<<<< HEAD
========
class MetadataLedgerSerializer(serializers.Serializer):
=======
class MetadataLedgerSerializer(serializers.ModelSerializer):
>>>>>>> d4f8b38 (Adding XIA to XIS metadata_ledger using REST_API.)
    """Serializes an entry into the Metadata Ledger"""
    class Meta:
<<<<<<< HEAD
<<<<<<< HEAD
=======


=======
>>>>>>> aaa8cae (Commits before rebase)
class MetadataLedgerSerializer(serializers.Serializer):
=======
class MetadataLedgerSerializer(serializers.ModelSerializer):
>>>>>>> 0d964ae (ECC-420 Validation of metadata in XIS request)
    """Serializes an entry into the Metadata Ledger"""

    class Meta:
<<<<<<< HEAD

>>>>>>> 33f1bd1 (ECC - 420 Implemented validation on request data & sending response accordingly)
=======

<<<<<<<< HEAD:app/api/serializers.py
# 2. SupplementalLedgerSerializer
========
class MetadataLedgerSerializer(serializers.Serializer):
=======
class MetadataLedgerSerializer(serializers.ModelSerializer):
>>>>>>> d4f8b38 (Adding XIA to XIS metadata_ledger using REST_API.)
    """Serializes an entry into the Metadata Ledger"""
    class Meta:
>>>>>>> 21f2f28 (added new core app; fixed secret key docker config)
        model = models.MetadataLedger
            fields = ('unique_record_identifier',
                      'agent_name',
                      'date_inserted',
                      'metadata_key',
                      'metadata_hash',
                      'metadata',
                      'record_status',
                      'date_deleted',
                      'metadata_validation_date',
                      'metadata_validation_status')
            extra_kwargs: {
                'unique_record_identifier': {'max_length':50,
                                             'primary_key':True,
                                             'editable':False},
                'agent_name': {'max_length':255},
                'date_inserted': {'blank':True, 'null':True},
                'metadata_hash': {'max_length':200},
                'metadata': {'blank'=True},
                'record_status': {'max_length': 10,
                                  'blank': True,
                                  'choices': RECORD_ACTIVATION_STATUS_CHOICES
                                  },
                'date_deleted': {'blank': True, 'null': True},
                'metadata_validation_date': {'blank': True, 'null': True},
                'metadata_validation_status': {'max_length': 10,
                                               'blank': True,
                                               'choices': MetadataLedger.METADATA_VALIDATION_CHOICES},
                }
<<<<<<< HEAD
<<<<<<< HEAD
=======
        model = MetadataLedger
<<<<<<< HEAD
<<<<<<< HEAD
=======
        model = MetadataLedger
>>>>>>> 01f0bef (Update models.py and serializers.py)
        fields = ('unique_record_identifier',
                  'agent_name',
                  'date_inserted',
                  'metadata_key',
                  'metadata_hash',
                  'metadata',
                  'record_status',
                  'date_deleted',
                  'metadata_validation_date',
                  'metadata_validation_status')
        extra_kwargs: {
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8b66375 (Made corrections to serializers.py and views.py.)
            'unique_record_identifier': {'max_length': 50},
            'agent_name': {'max_length': 255},
            'date_inserted': {'blank': True, 'null': True},
            'metadata_hash': {'max_length': 200},
            'metadata': {'blank': True},
<<<<<<< HEAD
=======
            'unique_record_identifier': {'max_length':50},
            'agent_name': {'max_length':255},
            'date_inserted': {'blank':True, 'null':True},
            'metadata_hash': {'max_length':200},
            'metadata': {'blank':True},
>>>>>>> 01f0bef (Update models.py and serializers.py)
=======
>>>>>>> 8b66375 (Made corrections to serializers.py and views.py.)
            'record_status': {'max_length': 10,
                              'blank': True,
                              'choices': MetadataLedger.RECORD_ACTIVATION_STATUS_CHOICES
                              },
            'date_deleted': {'blank': True, 'null': True},
            'metadata_validation_date': {'blank': True, 'null': True},
            'metadata_validation_status': {'max_length': 10,
                                           'blank': True,
                                           'choices': MetadataLedger.METADATA_VALIDATION_CHOICES},
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            }
>>>>>>> 01f0bef (Update models.py and serializers.py)
=======
        }
>>>>>>> 8b66375 (Made corrections to serializers.py and views.py.)
=======

        model = MetadataLedger


>>>>>>> 33f1bd1 (ECC - 420 Implemented validation on request data & sending response accordingly)
=======
>>>>>>> 21f2f28 (added new core app; fixed secret key docker config)
=======
            }
>>>>>>> 01f0bef (Update models.py and serializers.py)
=======
        }
>>>>>>> 8b66375 (Made corrections to serializers.py and views.py.)


class SupplementalLedgerSerializer(serializers.Serializer):
    """Serializes an entry into the Supplemental Ledger"""
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8b66375 (Made corrections to serializers.py and views.py.)

    class Meta:
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======

>>>>>>> 33f1bd1 (ECC - 420 Implemented validation on request data & sending response accordingly)
=======
    class Meta:
>>>>>>> 21f2f28 (added new core app; fixed secret key docker config)
        model = models.SupplementalLedger
            fields = ('unique_record_identifier',
                      'agent_name',
                      'date_inserted',
                      'metadata_key',
                      'metadata_hash',
                      'metadata',
                      'record_status',
                      'date_deleted',
                      'metadata_validation_date',
                      'metadata_validation_status')
            extra_kwargs: {
                'unique_record_identifier': {'max_length':50,
                                             'primary_key':True,
                                             'editable':False},
                'agent_name': {'max_length':255},
                'date_inserted': {'blank':True, 'null':True},
                'metadata_hash': {'max_length':200},
                'metadata': {'blank'=True},
                'record_status': {'max_length': 10,
                                  'blank': True,
                                  'choices': RECORD_ACTIVATION_STATUS_CHOICES
                                  },
                'date_deleted': {'blank': True, 'null': True},
                'metadata_validation_date': {'blank': True, 'null': True},
                'metadata_validation_status': {'max_length': 10,
                                               'blank': True,
                                               'choices': SupplementalLedger.METADATA_VALIDATION_CHOICES},
                }
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>>> 21f2f28 (added new core app; fixed secret key docker config):app/metadata_api/serializers.py
>>>>>>> 21f2f28 (added new core app; fixed secret key docker config)
=======
        model = SupplementalLedger
        fields = ('unique_record_identifier',
                  'agent_name',
=======

        fields = ['unique_record_identifier',
                  'provider_name',
>>>>>>> d4f8b38 (Adding XIA to XIS metadata_ledger using REST_API.)
=======

class SupplementalLedgerSerializer(serializers.ModelSerializer):
    """Serializes an entry into the Supplemental Ledger"""

    class Meta:
        model = SupplementalLedger
        fields = ['unique_record_identifier',
                  'agent_name',
>>>>>>> 0d964ae (ECC-420 Validation of metadata in XIS request)
=======

        model = SupplementalLedger
        fields = ('unique_record_identifier',
                  'agent_name',

>>>>>>> 33f1bd1 (ECC - 420 Implemented validation on request data & sending response accordingly)
=======
        model = MetadataLedger

        fields = ['unique_record_identifier',
                  'provider_name',
>>>>>>> aaa8cae (Commits before rebase)
=======
        model = SupplementalLedger
        fields = ('unique_record_identifier',
                  'agent_name',
>>>>>>> 01f0bef (Update models.py and serializers.py)
=======

        fields = ['unique_record_identifier',
                  'provider_name',
>>>>>>> d4f8b38 (Adding XIA to XIS metadata_ledger using REST_API.)
                  'date_inserted',
                  'metadata_key',
                  'metadata_hash',
                  'metadata',
                  'record_status',
                  'date_deleted',
                  'metadata_validation_date',
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 33f1bd1 (ECC - 420 Implemented validation on request data & sending response accordingly)
                  'metadata_validation_status')
        extra_kwargs: {
            'unique_record_identifier': {'max_length': 50},
            'agent_name': {'max_length': 255},
            'date_inserted': {'blank': True, 'null': True},
            'metadata_hash': {'max_length': 200},
            'metadata': {'blank': True},
=======
                  'metadata_validation_status')
        extra_kwargs: {
<<<<<<< HEAD
            'unique_record_identifier': {'max_length':50},
            'agent_name': {'max_length':255},
            'date_inserted': {'blank':True, 'null':True},
            'metadata_hash': {'max_length':200},
            'metadata': {'blank':True},
>>>>>>> 01f0bef (Update models.py and serializers.py)
=======
            'unique_record_identifier': {'max_length': 50},
            'agent_name': {'max_length': 255},
            'date_inserted': {'blank': True, 'null': True},
            'metadata_hash': {'max_length': 200},
            'metadata': {'blank': True},
>>>>>>> 8b66375 (Made corrections to serializers.py and views.py.)
            'record_status': {'max_length': 10,
                              'blank': True,
                              'choices': SupplementalLedger.RECORD_ACTIVATION_STATUS_CHOICES
                              },
            'date_deleted': {'blank': True, 'null': True},
            'metadata_validation_date': {'blank': True, 'null': True},
            'metadata_validation_status': {'max_length': 10,
                                           'blank': True,
                                           'choices': SupplementalLedger.METADATA_VALIDATION_CHOICES},
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            }
>>>>>>> 01f0bef (Update models.py and serializers.py)
=======
        }
>>>>>>> 8b66375 (Made corrections to serializers.py and views.py.)
=======
                  'metadata_validation_status']
=======

            }



=======
>>>>>>> aaa8cae (Commits before rebase)
                  'metadata_validation_status']

    def validate(self, data):
        """function to validate metadata field"""

        # Call function to get required & recommended values
        required_dict, recommended_dict = \
            get_required_recommended_fields_for_target_validation()
        json_metadata = data.get('metadata')
        for column in json_metadata:
            required_columns = required_dict[column]
            recommended_columns = recommended_dict[column]
            validation_result = 'Y'
            for key in json_metadata[column]:
                if key in required_columns:
                    if not json_metadata[column][key]:
                        validation_result = 'N'
                        logger.info(
                            "Record " + str(
                                data.get('unique_record_identifier')
                            ) + "does not have all "
                                "REQUIRED "
                                "fields. " + key + "field"
                                                   " is "
                                                   " empty")
                    if key in recommended_columns:
                        if not json_metadata[column][key]:
                            logger.info(
                                "Record " + str(
                                    data.unique_record_identifier) +
                                " does not have all RECOMMENDED fields. " +
                                key + " field is empty")
        data['metadata_validation_status'] = validation_result
        data['metadata_validation_date'] = timezone.now()
        logger.info(data['metadata_validation_status'],
                    data['metadata_validation_date'])
        return data

<<<<<<< HEAD
>>>>>>> 33f1bd1 (ECC - 420 Implemented validation on request data & sending response accordingly)
=======
                  'metadata_validation_status']
>>>>>>> d4f8b38 (Adding XIA to XIS metadata_ledger using REST_API.)
# class SupplementalLedgerSerializer(serializers.Serializer):
#     """Serializes an entry into the Supplemental Ledger"""
#
#     class Meta:
#         model = SupplementalLedger
#         fields = ('unique_record_identifier',
#                   'agent_name',
#                   'date_inserted',
#                   'metadata_key',
#                   'metadata_hash',
#                   'metadata',
#                   'record_status',
#                   'date_deleted',
#                   'metadata_validation_date',
#                   'metadata_validation_status')
#         extra_kwargs:{
#             'unique_record_identifier': {'max_length': 50},
#             'agent_name': {'max_length': 255},
#             'date_inserted': {'blank': True, 'null': True},
#             'metadata_hash': {'max_length': 200},
#             'metadata': {'blank': True},
#             'record_status': {'max_length': 10,
#                               'blank': True,
#                               'choices': SupplementalLedger.RECORD_ACTIVATION_STATUS_CHOICES
#                               },
#             'date_deleted': {'blank': True, 'null': True},
#             'metadata_validation_date': {'blank': True, 'null': True},
#             'metadata_validation_status': {'max_length': 10,
#                                            'blank': True,
#                                            'choices': SupplementalLedger.METADATA_VALIDATION_CHOICES}
#         }
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d4f8b38 (Adding XIA to XIS metadata_ledger using REST_API.)
=======
                  'metadata_validation_status']
>>>>>>> 0d964ae (ECC-420 Validation of metadata in XIS request)
=======

>>>>>>> 33f1bd1 (ECC - 420 Implemented validation on request data & sending response accordingly)
=======
>>>>>>> aaa8cae (Commits before rebase)
=======
>>>>>>>> 21f2f28 (added new core app; fixed secret key docker config):app/metadata_api/serializers.py
>>>>>>> 21f2f28 (added new core app; fixed secret key docker config)
=======
            }
>>>>>>> 01f0bef (Update models.py and serializers.py)
=======
        }
>>>>>>> 8b66375 (Made corrections to serializers.py and views.py.)
=======
>>>>>>> d4f8b38 (Adding XIA to XIS metadata_ledger using REST_API.)
=======

class SupplementalLedgerSerializer(serializers.ModelSerializer):
    """Serializes an entry into the Supplemental Ledger"""

    class Meta:
        model = SupplementalLedger
        fields = ['unique_record_identifier',
                  'agent_name',
                  'date_inserted',
                  'metadata_key',
                  'metadata_hash',
                  'metadata',
                  'record_status',
                  'date_deleted',
                  'metadata_validation_date',
                  'metadata_validation_status']
>>>>>>> 0d964ae (ECC-420 Validation of metadata in XIS request)
