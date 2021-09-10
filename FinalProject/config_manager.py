from definitions import PROJECT_ROOT_DIR
import configparser
import os
import boto3

_config = configparser.ConfigParser()

_config.read(os.path.join(PROJECT_ROOT_DIR, 'config.ini'))

S3_BUCKET = _config['default']['url']
S3_CLIENT = boto3.client('s3')
S3_RESOURCE = boto3.resource('s3')

BUCKET_CONTENTS_TALENT = S3_CLIENT.list_objects_v2(
        Bucket=S3_BUCKET,
        Prefix='Talent'
    )

BUCKET_CONTENTS_ACADEMY = S3_CLIENT.list_objects_v2(
        Bucket=S3_BUCKET,
        Prefix='Academy'
    )
