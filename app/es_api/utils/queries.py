from elasticsearch_dsl import connections, Search, Q
from requests.exceptions import HTTPError 
import json
import logging

connections.create_connection(alias='default',
    hosts=['3.208.136.89:9200'], timeout=60)

logger = logging.getLogger('dict_config_logger')

def search_by_keyword(keyword=""):
    """This method takes in a keyword string and queries ElasticSearch for the
        term then returns the dictionary results"""
    q = Q("bool", should=[Q("match", Course__CourseDescription=keyword),       
        Q("match", Course__CourseTitle=keyword)], minimum_should_match=1)  
    s = Search(using='default', index="dau-test").query(q)
    response = s.execute()
    logger.info(response)  
    searchResults = get_results(response)

    return searchResults  

def get_results(response):
    """This helper method consumes the response of an ElasticSearch Query and
        adds the hits to an array then returns a dictionary representing the
        results""" 
    hit_arr = [] 

    for hit in response: 
        hit_dict = hit.to_dict()
        jsonObj = json.dumps(hit_dict)   
        hit_arr.append(hit_dict)
        # result_tuple = (hit.firstname + ' ' + hit.lastname,
        # hit.email, hit.gender, hit.address)    
        # results.append(result_tuple)  

    resultObj = {
        "hits": hit_arr,
        "total": response.hits.total.value
    }
    return json.dumps(resultObj)

# if __name__ == '__main__':  
#     print("Opal guy details:\n", search_by_keyword(keyword = "connection"))
