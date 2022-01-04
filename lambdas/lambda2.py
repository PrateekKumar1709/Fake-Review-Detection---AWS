import requests
import json
import numpy as np
import pickle
import boto3
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from datetime import datetime

s3 = boto3.resource('s3')
vectorizer = pickle.loads(s3.Bucket("fake-review").Object("vectorizer.pkl").get()['Body'].read())
print(vectorizer)

s3 = boto3.resource('s3')
sk_nblearn = pickle.loads(s3.Bucket("fake-review").Object("sk_nblearn.pkl").get()['Body'].read())
print(sk_nblearn)

client = boto3.client('comprehend')


def lambda_handler(event, context):
    zeroes = ones = 0
    rev = event
    result = json.dumps(rev)
    tsaa=event['review'][0]
    print(event)
    time=datetime.now().isoformat(timespec='seconds')
    sa = client.detect_sentiment(Text=tsaa,LanguageCode='en')['Sentiment']
    #print(sa)
    words = [word for word in result.split() if word.lower() not in ENGLISH_STOP_WORDS]
    new_text = " ".join(words)
    res=list(new_text.split(" "))
    #print(type(res))
    X_rev_idf = vectorizer.transform(res)
    #print("! -- ", X_rev_idf.shape[0] == len(res))
    prediction = sk_nblearn.predict(X_rev_idf)
    probablity = sk_nblearn.predict_proba(X_rev_idf)
    
    for x in prediction:
        if x==0:
            zeroes+=1
        else:
            ones+=1
    
    if ones>zeroes:
        reviewResult='Fake'
    else:
        reviewResult='Authentic'

    print("results: ")
    resultProbability=np.max(probablity)
    print(reviewResult, resultProbability)
    
    format = {'reviewResult': reviewResult, 'resultProbability': resultProbability, 'sentiment': sa , 'time':time ,'Review': rev}
    url = 'https://search-fakereview-fjhl4wim7nopif7k7qvdt4wbga.us-east-1.es.amazonaws.com/fake-review/_doc'
    headers = {"Content-Type": "application/json"}
    
    r = requests.post(url, data=json.dumps(format).encode(
        "utf-8"), headers=headers, auth=('prateek', 'Prateek@1709'))
    print(r.text)
    
    return {
        'result': [{
        'reviewResult':reviewResult,
        'resultProbability':resultProbability,
        }]
    }

 
    
