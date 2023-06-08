import json
import logging

import bleach
from dateutil.parser import parse

logger = logging.getLogger('dict_config_logger')


def required_recommended_logs(id_num, category, field):
    """logs the missing required and recommended """

    # Logs the missing required columns
    if category == 'Required':
        logger.error(
            "Record " + str(
                id_num) + " does not have all " + category +
            " fields. "
            + field + " field is empty")

    # Logs the missing recommended columns
    if category == 'Recommended':
        logger.warning(
            "Record " + str(
                id_num) + " does not have all " + category +
            " fields. "
            + field + " field is empty")

    # Logs the inaccurate datatype columns
    if category == 'datatype':
        logger.warning(
            "Record " + str(
                id_num) + " does not have the expected " + category +
            " for the field " + field)


def dict_flatten(data_dict, required_column_list):
    """Function to flatten/normalize  data dictionary"""

    # assign flattened json object to variable
    flatten_dict = {}

    # Check every key elements value in data
    for element in data_dict:
        # If Json Field value is a Nested Json
        if isinstance(data_dict[element], dict):
            flatten_dict_object(data_dict[element],
                                element, flatten_dict, required_column_list)
        # If Json Field value is a list
        elif isinstance(data_dict[element], list):
            flatten_list_object(data_dict[element],
                                element, flatten_dict, required_column_list)
        # If Json Field value is a string
        else:
            update_flattened_object(data_dict[element],
                                    element, flatten_dict)

    # Return the flattened json object
    return flatten_dict


def is_date(string, fuzzy=False):
    """
    Return whether the string can be interpreted as a date.

    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
    """
    if isinstance(string, str):
        try:
            parse(string, fuzzy=fuzzy)
            return True

        except ValueError:
            return False
    else:
        return False


def flatten_list_object(list_obj, prefix, flatten_dict, required_column_list):
    """function to flatten list object"""
    required_prefix_list = []
    for i in range(len(list_obj)):
        #  storing initial flatten_dict for resetting values
        if not i:
            flatten_dict_temp = flatten_dict
        # resetting flatten_dict to initial value
        else:
            flatten_dict = flatten_dict_temp

        passed = flatten_list_object_helper(list_obj, prefix, flatten_dict,
                                            required_column_list,
                                            required_prefix_list, i)

        # if all required values are skip other object in list
        if passed:
            break


def flatten_list_object_helper(list_obj, prefix, flatten_dict,
                               required_column_list, required_prefix_list, i):
    if isinstance(list_obj[i], list):
        flatten_list_object(list_obj[i], prefix, flatten_dict,
                            required_column_list)

    elif isinstance(list_obj[i], dict):
        flatten_dict_object(list_obj[i], prefix, flatten_dict,
                            required_column_list)

    else:
        update_flattened_object(list_obj[i], prefix, flatten_dict)

        # looping through required column names
    for required_prefix in required_column_list:
        # finding matching value along with index
        if prefix in required_prefix and\
                required_prefix.index(prefix) == 0:
            required_prefix_list.append(required_prefix)
        #  setting up flag for checking validation
    passed = True

    # looping through items in required columns with matching prefix
    for item_to_check in required_prefix_list:
        #  flag if value not found
        if not flatten_dict[item_to_check]:
            passed = False
    return passed


def flatten_dict_object(dict_obj, prefix, flatten_dict, required_column_list):
    """function to flatten dictionary object"""
    for element in dict_obj:
        if isinstance(dict_obj[element], dict):
            flatten_dict_object(dict_obj[element], prefix + "." +
                                element, flatten_dict, required_column_list)

        elif isinstance(dict_obj[element], list):
            flatten_list_object(dict_obj[element], prefix + "." +
                                element, flatten_dict, required_column_list)

        else:
            update_flattened_object(dict_obj[element], prefix + "." +
                                    element, flatten_dict)


def update_flattened_object(str_obj, prefix, flatten_dict):
    """function to update flattened object to dict variable"""

    flatten_dict.update({prefix: str_obj})


def update_multilevel_dict(dictionary, path, value):
    """
    recursive function to traverse dict to path and set value
    :param dictionary: the dictionary to insert into
    :param path: a list of keys to navigate through to the final item
    :param value: the value to store
    :return: returns the updated dictionary
    """

    if path == []:
        return value

    if path[0] not in dictionary:
        dictionary[path[0]] = {}

    dictionary.update(
        {
            path[0]:
                update_multilevel_dict(dictionary[path[0]], path[1:], value)
        }
    )

    return dictionary


def multi_dict_sort(data, sort_type=0):
    """
    Sorts a dictionary with multiple sub-dictionaries.
    :param data: dictionary to sort
    :param sort_type: for key sort use 0 [default]; for value sort use 1
    :return: dict
    """
    if data:
        items_list = [key for (key, value) in data.items()
                      if type(value) is dict]
        for item_key in items_list:
            data[item_key] = multi_dict_sort(data[item_key], sort_type)
        return {key: value for (key, value) in sorted(data.items(),
                                                      key=lambda x:
                                                      x[sort_type])}
    return data


def bleach_data_to_json(rdata):
    """Function to bleach/clean HTML tags from data and
    return dictionary data"""

    # bleaching/cleaning HTML tag data
    bdata = (bleach.clean(str(rdata), strip=True))

    # Converting data to json acceptable format
    json_acceptable_string = bdata.replace("'", "\"")

    # Loading json dtring to dict format
    metadata = json.loads(json_acceptable_string)

    return metadata
