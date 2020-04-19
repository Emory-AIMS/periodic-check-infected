
import sys

SQS_QUE_URL_PATIENTS = 'https://sqs.us-east-1.amazonaws.com/746726732930/doctor-infected'
SQS_QUE_URL_NOTIFICATIONS = 'https://sqs.us-east-1.amazonaws.com/746726732930/potential-infected-notification'
SQS_QUE_URL_DEAD_LETTERS = 'https://sqs.us-east-1.amazonaws.com/746726732930/doctor-infected-dead-letter'


def get_sqs_patients_url():
    return SQS_QUE_URL_PATIENTS


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
