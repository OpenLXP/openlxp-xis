import json
import logging
import os

import boto3
from core.management.utils.xis_internal import dict_flatten
from core.models import XISConfiguration

logger = logging.getLogger('dict_config_logger')


def aws_get():
    """Function to get aws bucket name from env file"""
    bucket_name = os.environ.get('BUCKET_NAME')
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
    """Retrieve target validation schema from XIS configuration """
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
            if column.endswith(".use"):
                column = column[:-len(".use")]
            required_column_list.append(column)
        elif value == "Recommended":
            if column.endswith(".use"):
                column = column[:-len(".use")]
            recommended_column_list.append(column)

    # Returning required and recommended list for validation
    return required_column_list, recommended_column_list


def get_optional_fields_for_validation():
    """Creating list of fields which are Optional"""

    schema_data_dict = get_target_validation_schema()
    # Call function to flatten schema used for validation
    flattened_schema_dict = dict_flatten(schema_data_dict, [])

    # Declare list for optional column names
    optional_column_list = list()

    #  Adding values to optional list based on schema
    for column, value in flattened_schema_dict.items():
        if value == "Optional":
            if column.endswith(".use"):
                column = column[:-len(".use")]
            optional_column_list.append(column)

    # Returning optional list for validation
    return optional_column_list


def get_data_types_for_validation():
    """Creating list of fields with the expected datatype objects"""

    schema_data_dict = get_target_validation_schema()
    # Call function to flatten schema used for validation
    flattened_schema_dict = dict_flatten(schema_data_dict, [])

    # mapping from string to datatype objects
    datatype_to_object = {
        "int": int,
        "str": str,
        "bool": bool
    }
    expected_data_types = dict()

    #  updating dictionary with expected datatype values for fields in metadata
    for column, value in flattened_schema_dict.items():
        if column.endswith(".data_type"):
            key = column[:-len(".data_type")]
            if value in datatype_to_object:
                value = datatype_to_object[value]
            expected_data_types.update({key: value})

    # Returning required and recommended list for validation
    return expected_data_types
