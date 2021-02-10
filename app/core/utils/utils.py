<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
import hashlib
>>>>>>> 96c3f05 (added configuration model; added validation helper functions)
=======
>>>>>>> 33f1bd1 (ECC - 420 Implemented validation on request data & sending response accordingly)
=======
import hashlib
>>>>>>> 96c3f05 (added configuration model; added validation helper functions)
import logging
import boto3
import json
import pandas as pd
from django.core.management.base import BaseCommand
from core.models import XISConfiguration
from django.utils import timezone

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
logger = logging.getLogger('dict_config_logger')

=======

logger = logging.getLogger('dict_config_logger')
>>>>>>> 96c3f05 (added configuration model; added validation helper functions)
=======
logger = logging.getLogger('dict_config_logger')

>>>>>>> 33f1bd1 (ECC - 420 Implemented validation on request data & sending response accordingly)
=======

logger = logging.getLogger('dict_config_logger')
>>>>>>> 96c3f05 (added configuration model; added validation helper functions)

def aws_get():
    bucket_name = 'dauxsr'
    source_file_name = 'DAU_Consolidated.csv'
    source_schema = 'DAU_Source_Renaming_Schema.json'
    return bucket_name, source_file_name, source_schema


def read_source_file():
    """setting file path from s3 bucket"""
    bucket_name, source_file_name, source_schema = aws_get()
    source_file_path = 's3://%s/%s/' % (bucket_name, source_file_name)
    source_data_dict = read_json_data(source_schema)

    logger.info("Retrieving data from XSR")
    source_df = pd.read_csv(source_file_path)
    logger.info("Renaming column values of Data from source")
    std_replaced_nan_df = source_df.where(pd.notnull(source_df),
                                          None)
    std_source_df = std_replaced_nan_df.rename(columns=source_data_dict)

    return std_source_df


def read_json_data(file_name):
    """setting file path for json files and ingesting as dictionary values """
    s3 = boto3.resource('s3')
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    bucket_name, x, y = aws_get()
=======
    bucket_name,x,y = aws_get()
>>>>>>> 96c3f05 (added configuration model; added validation helper functions)
=======
    bucket_name, x, y = aws_get()
>>>>>>> 33f1bd1 (ECC - 420 Implemented validation on request data & sending response accordingly)
=======
    bucket_name,x,y = aws_get()
>>>>>>> 96c3f05 (added configuration model; added validation helper functions)

    json_path = s3.Object(bucket_name, file_name)
    json_content = json_path.get()['Body'].read().decode('utf-8')
    data_dict = json.loads(json_content)
    return data_dict

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

=======
>>>>>>> 96c3f05 (added configuration model; added validation helper functions)
=======

>>>>>>> 33f1bd1 (ECC - 420 Implemented validation on request data & sending response accordingly)
=======
>>>>>>> 96c3f05 (added configuration model; added validation helper functions)
def get_target_validation_schema():
    """Retrieve target validation schema from XIA configuration """
    logger.info("Configuration of schemas and files")
    data = XISConfiguration.objects.first()
    target_validation_schema = data.target_metadata_schema
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 96c3f05 (added configuration model; added validation helper functions)
    return target_validation_schema


def read_target_validation_schema(target_validation_schema):
    """Creating dictionary from schema"""
<<<<<<< HEAD
>>>>>>> 96c3f05 (added configuration model; added validation helper functions)
=======
>>>>>>> 33f1bd1 (ECC - 420 Implemented validation on request data & sending response accordingly)
=======
>>>>>>> 96c3f05 (added configuration model; added validation helper functions)
    logger.info("Reading schema for validation")
    # Read source validation schema as dictionary
    schema_data_dict = read_json_data(target_validation_schema)
    return schema_data_dict

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 33f1bd1 (ECC - 420 Implemented validation on request data & sending response accordingly)

def get_required_recommended_fields_for_target_validation():
    """Creating list of fields which are Required & Recommended"""

    # Call function to get target validation dictionary
    schema_data_dict = get_target_validation_schema()

<<<<<<< HEAD
=======
def get_required_recommended_fields_for_target_validation(schema_data_dict):
    """Creating list of fields which are Required & Recommended"""
>>>>>>> 96c3f05 (added configuration model; added validation helper functions)
=======
>>>>>>> 33f1bd1 (ECC - 420 Implemented validation on request data & sending response accordingly)
=======
def get_required_recommended_fields_for_target_validation(schema_data_dict):
    """Creating list of fields which are Required & Recommended"""
>>>>>>> 96c3f05 (added configuration model; added validation helper functions)
    required_dict = {}
    recommended_dict = {}

    # Getting key list whose Value is Required
    for k in schema_data_dict:
        required_list = []
        recommended_list = []
        for k1, v1 in schema_data_dict[k].items():
            if v1 == 'Required':
                required_list.append(k1)
            if v1 == 'Recommended':
                recommended_list.append(k1)

            required_dict[k] = required_list

            recommended_dict[k] = recommended_list

    return required_dict, recommended_dict
