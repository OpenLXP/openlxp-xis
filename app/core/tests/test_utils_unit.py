from unittest.mock import patch

from core.utils.xis_internal import (dict_flatten, update_flattened_object,
                                     flatten_dict_object, flatten_list_object)
from ddt import data, ddt
from django.test import tag

from core.models import XISConfiguration
from core.utils.xse_client import (get_elasticsearch_endpoint,
                                   get_elasticsearch_index)
from .test_setup import TestSetUp


@tag('unit')
@ddt
class UtilsTests(TestSetUp):
    """This cases for xis_internal.py"""

    def test_dict_flatten(self):
        """Test function to navigate to value in source
        metadata to be validated"""
        test_data_dict = {"key1": "value1",
                          "key2": {"sub_key1": "sub_value1"},
                          "key3": [{"sub_key2": "sub_value2"},
                                   {"sub_key3": "sub_value3"}]}

        with patch('core.utils.xis_internal.flatten_list_object') \
                as mock_flatten_list, \
                patch('core.utils.xis_internal.flatten_dict_'
                      'object') as mock_flatten_dict, \
                patch('core.utils.xis_internal.update_flattened_'
                      'object') as mock_update_flattened:
            mock_flatten_list.return_value = mock_flatten_list
            mock_flatten_list.return_value = None
            mock_flatten_dict.return_value = mock_flatten_dict
            mock_flatten_dict.return_value = None
            mock_update_flattened.return_value = mock_update_flattened
            mock_update_flattened.return_value = None

        return_value = dict_flatten(test_data_dict,
                                    self.test_required_column_names)
        self.assertTrue(return_value)

    @data(
        ([{'a.b': None, 'a.c': 'value2', 'd': None},
          {'a.b': 'value1', 'a.c': 'value2', 'd': None}]))
    def test_flatten_list_object_loop(self, value):
        """Test the looping od the function to flatten
        list object when the value is list"""
        prefix = 'a'
        flatten_dict = {}
        required_list = ['a.b', 'a.c', 'd']
        with patch('core.utils.xis_internal.flatten_list_object') \
                as mock_flatten_list, \
                patch('core.utils.xis_internal.flatten_dict_'
                      'object') as mock_flatten_dict, \
                patch('core.utils.xis_internal.update_flattened_'
                      'object') as mock_update_flattened:
            mock_flatten_list.return_value = mock_flatten_list
            mock_flatten_list.return_value = None
            mock_flatten_dict.return_value = mock_flatten_dict
            mock_flatten_dict.return_value = None
            mock_update_flattened.side_effect = flatten_dict = \
                {'a.b': None, 'a.c': 'value2'}

            flatten_list_object(value, prefix, flatten_dict, required_list)
            self.assertEqual(mock_flatten_dict.call_count, 2)

    @data(
        ([{'b': [None]}]))
    def test_flatten_list_object_multilevel(self, value):
        """Test the function to flatten list object
         when the value is list for multilevel lists"""
        prefix = 'a'
        flatten_dict = {}
        required_list = ['a.b', 'd']
        with patch('core.utils.xis_internal.flatten_list_object') \
                as mock_flatten_list, \
                patch('core.utils.xis_internal.flatten_dict_'
                      'object') as mock_flatten_dict, \
                patch('core.utils.xis_internal.update_flattened_'
                      'object') as mock_update_flattened:
            mock_flatten_list.return_value = mock_update_flattened
            mock_flatten_dict.return_value = mock_flatten_list()
            mock_update_flattened.side_effect = flatten_dict = \
                {'a.b': None}

            flatten_list_object(value, prefix, flatten_dict, required_list)
            self.assertEqual(mock_flatten_list.call_count, 1)

    @data(([{'A': 'a'}]), ([{'B': 'b', 'C': 'c'}]))
    def test_flatten_list_object_list(self, value):
        """Test the function to flatten list object when the value is list"""
        prefix = 'test'
        flatten_dict = []
        with patch('core.utils.xis_internal.flatten_list_object') \
                as mock_flatten_list, \
                patch('core.utils.xis_internal.flatten_dict_'
                      'object') as mock_flatten_dict, \
                patch('core.utils.xis_internal.update_flattened_'
                      'object') as mock_update_flattened:
            mock_flatten_list.return_value = mock_flatten_list
            mock_flatten_list.return_value = None
            mock_flatten_dict.return_value = mock_flatten_dict
            mock_flatten_dict.return_value = None
            mock_update_flattened.return_value = mock_update_flattened
            mock_update_flattened.return_value = None

            flatten_list_object(value, prefix, flatten_dict,
                                self.test_required_column_names)

            self.assertEqual(mock_flatten_dict.call_count, 1)

    @data(([{'A': 'a'}]), ([{'B': 'b', 'C': 'c'}]))
    def test_flatten_list_object_dict(self, value):
        """Test the function to flatten list object when the value is dict"""
        prefix = 'test'
        flatten_dict = []
        with patch('core.utils.xis_internal.flatten_list_object') \
                as mock_flatten_list, \
                patch('core.utils.xis_internal.flatten_dict_'
                      'object') as mock_flatten_dict, \
                patch('core.utils.xis_internal.update_flattened_'
                      'object') as mock_update_flattened:
            mock_flatten_list.return_value = mock_flatten_list
            mock_flatten_list.return_value = None
            mock_flatten_dict.return_value = mock_flatten_dict
            mock_flatten_dict.return_value = None
            mock_update_flattened.return_value = mock_update_flattened
            mock_update_flattened.return_value = None

            flatten_list_object(value, prefix, flatten_dict,
                                self.test_required_column_names)

            self.assertEqual(mock_flatten_dict.call_count, 1)

    @data((['hello']), (['hi']))
    def test_flatten_list_object_str(self, value):
        """Test the function to flatten list object when the value is string"""
        prefix = 'test'
        flatten_dict = []
        with patch('core.utils.xis_internal.flatten_list_object') \
                as mock_flatten_list, \
                patch('core.utils.xis_internal.flatten_dict_'
                      'object') as mock_flatten_dict, \
                patch('core.utils.xis_internal.update_flattened_'
                      'object') as mock_update_flattened:
            mock_flatten_list.return_value = mock_flatten_list
            mock_flatten_list.return_value = None
            mock_flatten_dict.return_value = mock_flatten_dict
            mock_flatten_dict.return_value = None
            mock_update_flattened.return_value = mock_update_flattened
            mock_update_flattened.return_value = None
            flatten_list_object(value, prefix, flatten_dict,
                                self.test_required_column_names)

            self.assertEqual(mock_update_flattened.call_count, 1)

    @data(({'abc': {'A': 'a'}}), ({'xyz': {'B': 'b'}}))
    def test_flatten_dict_object_dict(self, value):
        """Test the function to flatten dictionary object when input value is
        a dict"""
        prefix = 'test'
        flatten_dict = []
        with patch('core.utils.xis_internal.flatten_list_object') \
                as mock_flatten_list, \
                patch('core.utils.xis_internal.flatten_dict_'
                      'object') as mock_flatten_dict, \
                patch('core.utils.xis_internal.update_flattened_'
                      'object') as mock_update_flattened:
            mock_flatten_list.return_value = mock_flatten_list
            mock_flatten_list.return_value = None
            mock_flatten_dict.return_value = mock_flatten_dict
            mock_flatten_dict.return_value = None
            mock_update_flattened.return_value = mock_update_flattened
            mock_update_flattened.return_value = None

            flatten_dict_object(value, prefix, flatten_dict,
                                self.test_required_column_names)

            self.assertEqual(mock_flatten_dict.call_count, 1)

    @data(({'abc': [1, 2, 3]}), ({'xyz': [1, 2, 3, 4, 5]}))
    def test_flatten_dict_object_list(self, value):
        """Test the function to flatten dictionary object when input value is
        a list"""
        prefix = 'test'
        flatten_dict = []
        with patch('core.utils.xis_internal.flatten_list_object') \
                as mock_flatten_list, \
                patch('core.utils.xis_internal.flatten_dict_'
                      'object') as mock_flatten_dict, \
                patch('core.utils.xis_internal.update_flattened_'
                      'object') as mock_update_flattened:
            mock_flatten_list.return_value = mock_flatten_list
            mock_flatten_list.return_value = None
            mock_flatten_dict.return_value = mock_flatten_dict
            mock_flatten_dict.return_value = None
            mock_update_flattened.return_value = mock_update_flattened
            mock_update_flattened.return_value = None

            flatten_dict_object(value, prefix, flatten_dict,
                                self.test_required_column_names)

            self.assertEqual(mock_flatten_list.call_count, 1)

    @data(({'abc': 'A'}), ({'xyz': 'B'}))
    def test_flatten_dict_object_str(self, value):
        """Test the function to flatten dictionary object when input value is
        a string"""
        prefix = 'test'
        flatten_dict = []
        with patch('core.utils.xis_internal.flatten_list_object') \
                as mock_flatten_list, \
                patch('core.utils.xis_internal.flatten_dict_'
                      'object') as mock_flatten_dict, \
                patch('core.utils.xis_internal.update_flattened_'
                      'object') as mock_update_flattened:
            mock_flatten_list.return_value = mock_flatten_list
            mock_flatten_list.return_value = None
            mock_flatten_dict.return_value = mock_flatten_dict
            mock_flatten_dict.return_value = None
            mock_update_flattened.return_value = mock_update_flattened
            mock_update_flattened.return_value = None

            flatten_dict_object(value, prefix, flatten_dict,
                                self.test_required_column_names)

            self.assertEqual(mock_update_flattened.call_count, 1)

    @data('', 'str1')
    def test_update_flattened_object(self, value):
        """Test the function which returns the source bucket name"""
        prefix = 'test'
        flatten_dict = {}
        update_flattened_object(value, prefix, flatten_dict)
        self.assertTrue(flatten_dict)

    """This cases for xse_client.py"""

    def test_get_elasticsearch_endpoint(self):
        """This test is to check if function returns the elasticsearch
        endpoint """
        with patch('core.utils.xse_client.XISConfiguration.objects') as \
                xis_config:
            configObj = XISConfiguration(target_schema="test.json",
                                         xse_host="host:8080",
                                         xse_index="test-index")
            xis_config.first.return_value = configObj
            result_api_es_endpoint = get_elasticsearch_endpoint()

            self.assertTrue(result_api_es_endpoint)

    def test_get_elasticsearch_index(self):
        """This test is to check if function returns the elasticsearch index"""
        with patch('core.utils.xse_client.XISConfiguration.objects') as \
                xis_config:
            configObj = XISConfiguration(target_schema="test.json",
                                         xse_host="host:8080",
                                         xse_index="test-index")
            xis_config.first.return_value = configObj
            result_api_es_index = get_elasticsearch_index()

            self.assertTrue(result_api_es_index)
