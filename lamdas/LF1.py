import json
import boto3
from botocore.vendored import requests
from requests_aws4auth import AWS4Auth
from utils import *
import datetime
import json
import os
import requests

import boto3
# Define the client to interact with Lex
client = boto3.client('lexv2-runtime')
def lambda_handler(event, context):
    print(event)
    print(context)


