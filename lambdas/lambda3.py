import json
import math
import dateutil.parser
import datetime
import time
import os
import logging
import boto3
import requests

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
headers = { "Content-Type": "application/json" }
host = "https://search-fakereview-fjhl4wim7nopif7k7qvdt4wbga.us-east-1.es.amazonaws.com/fake-review"
region = 'us-east-1'

def lambda_handler(event, context):
    #print("EVENT --- {}".format(json.dumps(event)))
    q1 = {
   "size": 1,
   "sort": { "time": "desc"},
   "query": {
      "match_all": {}
   }
}
    url = host + '/_search'
    r = requests.get(url, auth=('prateek', 'Prateek@1709'), headers=headers, data=json.dumps(q1))
    dict1 =  json.loads(r.text)
    reviewResult = dict1['hits']['hits'][0]['_source']['reviewResult']
    resultProbability = dict1['hits']['hits'][0]['_source']['resultProbability']
    #print(reviewResult)
    #print(resultProbability)
    return{
        'result': [{
        'reviewResult':reviewResult,
        'resultProbability':resultProbability,
        }]
    }