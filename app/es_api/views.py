from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse, HttpResponseBadRequest
from django.http import HttpResponseServerError
from rest_framework import status
from es_api.utils.queries import search_by_keyword
from requests.exceptions import HTTPError 
import json
import logging

logger = logging.getLogger('dict_config_logger')

def search_index(request):
    """This method defines an API for sending keyword queries to ElasticSearch
        without using a model""" 
    results = []
    keyword = ''

    if request.GET.get('keyword'):
        keyword = request.GET['keyword']

    if keyword != '':
        errorMsg = {
            "message": "error executing ElasticSearch query; " +
                "please check the logs"
        }
        errorMsgJSON = json.dumps(errorMsg)

        try:
            results = search_by_keyword(keyword = keyword)
        except HTTPError as http_err:
            logger.error(http_err)
            return HttpResponseServerError(errorMsgJSON, 
                content_type="application/json")
        except Exception as err:
            logger.error(err)
            return HttpResponseServerError(errorMsgJSON, 
                content_type="application/json")
        else:
            logger.info(results)
            return HttpResponse(results, content_type="application/json")
    else:
        error = {
            "message": "Request is missing 'keyword' query paramater"
        }
        errorJson = json.dumps(error)  
        return  HttpResponseBadRequest(errorJson, 
            content_type="application/json")
