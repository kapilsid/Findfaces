import json
import boto3
import os
import logging
from urllib.request import urlopen
import base64

log = logging.getLogger()
log.setLevel(logging.DEBUG)

#url = "https://scontent-bom1-1.xx.fbcdn.net/v/t1.0-9/11917782_938039246275692_2461622507350184663_n.jpg?_nc_cat=0&oh=6e58d7c9213b78d14a017563e97239ef&oe=5C25D83F"

region="us-east-1"

def faces(event,context):
    log.debug("Received event {}".format(json.dumps(event)))
    body = event['body']
    log.debug("Received event {}".format(body)) 
    d = json.loads(body)
    url = d['imgurl']
    log.debug("Received event {}".format(url))
   
    rekognition = boto3.client("rekognition",region)
  
    contents = urlopen(url).read()
    
    response = rekognition.detect_faces(
        Image ={
            "Bytes":contents,
        },
        Attributes=["ALL"],
    )
    
    return {
        'statusCode': 200,
		'headers': {
			"Access-Control-Allow-Origin" : "*" 
		},
        'body': json.dumps({'FaceDetails': response["FaceDetails"]})
    }

def objects(event,context):
    log.debug("Received event {}".format(json.dumps(event)))
    body = event['body']
    log.debug("Received event {}".format(body)) 
    d = json.loads(body)
    url = d['imgurl']
    log.debug("Received event {}".format(url))
   
   
    rekognition = boto3.client("rekognition",region)
  
    contents = urlopen(url).read()
    
    response = rekognition.detect_labels(
        Image ={
            "Bytes":contents,
        },
        MaxLabels=123,
        MinConfidence=70,
    )
    
    return {
        'statusCode': 200,
		'headers': {
			"Access-Control-Allow-Origin" : "*" 
		},
        'body': json.dumps({'Labels': response["Labels"]})
    }