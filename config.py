
import sys

SQS_QUE_URL_PATIENTS = 'https://sqs.us-west-1.amazonaws.com/018890560418/status-update'
AWS_REGION_NAME = 'us-west-1'

def get_sqs_patients_url():
    return SQS_QUE_URL_PATIENTS

def get_aws_region():
    return AWS_REGION_NAME

def get_db_user():
    if len(sys.argv) > 1:
        return sys.argv[1]
    return None


def get_db_password():
    if len(sys.argv) > 2:
        return sys.argv[2]
    return None


def get_timestamp_format_string():
    return '%Y-%m-%dT%H:%M:%S'


def days_look_back():
    return 14
