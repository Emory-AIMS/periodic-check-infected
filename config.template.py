import sys

SQS_REGION =                'like sa-east-1'
SQS_QUE_URL_PATIENTS =      'https://sqs.<region>.amazonaws.com/<account id>/doctor-infected'
SQS_QUE_URL_NOTIFICATIONS = 'https://sqs.<region>.amazonaws.com/<account id>/potential-infected-notification'
SQS_QUE_URL_DEAD_LETTERS =  'https://sqs.<region>.amazonaws.com/<account id>/doctor-infected-dead-letter'

# Username and Password are passed through CLI
DB_PORT =  3306
DB_HOST = "dbname"
DB_NAME = "dbinstance.rds.region.amazonaws.com"

def get_sqs_region():
    return SQS_REGION


def get_sqs_patients_url():
    return SQS_QUE_URL_PATIENTS


def get_db_port()
    return DB_PORT


def get_db_host()
    return DB_HOST


def get_db_name()
    return DB_NAME


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
