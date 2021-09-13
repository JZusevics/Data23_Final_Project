from Data23_Final_Project.definitions import PROJECT_ROOT_DIR
import configparser
import os
import boto3
import pandas as pd
from datetime import datetime
from ast import literal_eval
import json

# Parser
_config = configparser.ConfigParser()

# Config
_config.read(os.path.join(PROJECT_ROOT_DIR, 'config.ini'))

# Constants
S3_BUCKET = _config['default']['bucket_name']
S3_CLIENT = boto3.client('s3')
S3_RESOURCE = boto3.resource('s3')
BUCKET_CONTENTS_TALENT = S3_CLIENT.list_objects_v2(
        Bucket=S3_BUCKET,
        Prefix=_config['default']['talent']
    )
BUCKET_CONTENTS_ACADEMY = S3_CLIENT.list_objects_v2(
        Bucket=S3_BUCKET,
        Prefix=_config['default']['academy']
    )
TALENT_PAGINATOR = S3_CLIENT.get_paginator('list_objects_v2')
TALENT_PAGES = TALENT_PAGINATOR.paginate(
    Bucket=S3_BUCKET,
    Prefix=_config['default']['talent']
)
