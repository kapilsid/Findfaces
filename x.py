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
   
    url = event['imgurl']
    log.debug("Received event {}".format(url))
   
    rekognition = boto3.client("rekognition",region)
    #bucket = os.environ["BUCKET_NAME"]
    #bucket = event['Records'][0]['s3']['bucket']['name']
    #key = urllib.unquote_plus(
    #    event['Records'][0]['s3']['object']['key'].encode('utf8'))
    contents = urlopen(url).read()
    #image = base64.b64encode(contents)
    
    response = rekognition.detect_faces(
        Image ={
            "Bytes":contents,
        },
        Attributes=["ALL"],
    )


    # response = rekognition.detect_faces(
    #     Image ={
    #         "S3Object": {
    #             "Bucket":bucket,
    #             "Name":key
    #         },
    #     },
    #     Attributes=["ALL"],
    # )
    
    return {
        'statusCode': 200,
        'body': json.dumps({'FaceDetails': response["FaceDetails"]})
    }

  
