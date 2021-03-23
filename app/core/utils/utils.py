import json
import logging

import boto3
from core.models import XISConfiguration

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


def get_required_recommended_fields_for_target_validation():
    """Creating list of fields which are Required & Recommended"""
    # Call function to get target validation dictionary
    schema_data_dict = get_target_validation_schema()
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
