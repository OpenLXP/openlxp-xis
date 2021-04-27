import json
import logging

import boto3

from core.models import XISConfiguration
from core.utils.xis_internal import dict_flatten

logger = logging.getLogger('dict_config_logger')


def aws_get():
    bucket_name = 'xisschema'
    return bucket_name


def read_json_data(file_name):
    """setting file path for json files and ingesting as dictionary values """
    s3 = boto3.resource('s3')
    bucket_name = aws_get()
    json_path = s3.Object(bucket_name, file_name)
    json_content = json_path.get()['Body'].read().decode('utf-8')
    data_dict = json.loads(json_content)
    return data_dict


def get_target_validation_schema():
    """Retrieve target validation schema from XIA configuration """
    logger.info("Configuration of schemas and files")
    data = XISConfiguration.objects.first()
    target_validation_schema = data.target_schema
    logger.info("Reading schema for validation")
    # Read source validation schema as dictionary
    schema_data_dict = read_json_data(target_validation_schema)
    return schema_data_dict


def get_required_recommended_fields_for_validation():
    """Creating list of fields which are Required & Recommended"""

    schema_data_dict = get_target_validation_schema()
    # Call function to flatten schema used for validation
    flattened_schema_dict = dict_flatten(schema_data_dict, [])

    # Declare list for required and recommended column names
    required_column_list = list()
    recommended_column_list = list()

    #  Adding values to required and recommended list based on schema
    for column, value in flattened_schema_dict.items():
        if value == "Required":
            required_column_list.append(column)
        elif value == "Recommended":
            recommended_column_list.append(column)

    # Returning required and recommended list for validation
    return required_column_list, recommended_column_list
