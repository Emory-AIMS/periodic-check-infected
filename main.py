
import boto3
import json
import config
import mysql_handler
from datetime import datetime, timedelta

LIMIT_BATCH = 1000


def periodic_new_infected_interactions_check(debug=False):
    offset = 0
    continuation = True
    today = datetime.now()
    condition_infection = today - timedelta(config.days_look_back())

    sqs_client = boto3.resource('sqs', config.get_sqs_region())
    queue_infection = sqs_client.Queue(config.get_sqs_patients_url())

    while continuation:
        res = mysql_handler.get_infected(condition_infection, offset=offset, limit=LIMIT_BATCH, debug=debug)
        print('ANALYZING INFECTED LATER', res)
        if res is None or len(res) == 0:
            continuation = False
            break

        device_ids = []
        min_timestamp_analysis = today
        for entry in res:
            device_ids.append(str(entry['device_id']))
            min_timestamp_analysis = min(min_timestamp_analysis, entry['last_analysis_timestamp'])

        recurrent_infected = {
            'recurrent': {
                'device_ids': device_ids,
                'timestamp_min_unix': datetime.timestamp(min_timestamp_analysis)
            }
        }
        print('sending new message:', recurrent_infected)
        if not debug:
            queue_infection.send_message(MessageBody=json.dumps(recurrent_infected))

        print('updating current devices last timestamp')
        mysql_handler.update_last_analysis_timestamp(device_ids, today, debug=debug)
        offset += LIMIT_BATCH
        if debug:
            break


if __name__ == '__main__':
    # periodic_new_infected_interactions_check()
    periodic_new_infected_interactions_check(debug=True)
