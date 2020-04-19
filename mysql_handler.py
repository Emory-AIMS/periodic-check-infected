
import config
import pymysql
from dateutil import parser
from datetime import datetime

HOST = 'covid19-1.cblunr1bvwzp.us-east-1.rds.amazonaws.com'
PORT = 3306
DB = 'api_coronaviruscheck'

conn = None


def init_connection():
    global conn
    if conn is None:
        conn = pymysql.connect(
            host=HOST,
            user=config.get_db_user(),
            password=config.get_db_password(),
            port=PORT,
            db=DB,
            cursorclass=pymysql.cursors.DictCursor
        )


def close_connection():
    global conn
    if conn is not None:
        conn.close()
    conn = None


def get_connection():
    global conn
    if conn is None:
        init_connection()
    return conn


def get_infected(from_date, offset=0, limit=1000, debug=False):

    if debug:
        return [{
            'device_id': 1509,
            'infection_timestamp': parser.parse('2020-04-10T10:10:10'),
            'last_analysis_timestamp': parser.parse('2020-04-11T10:10:10')
        }]

    query = 'select * from infected_devices where infection_timestamp >= \'{}\' order by last_analysis_timestamp desc limit {} offset {}'\
        .format(from_date.strftime(config.get_timestamp_format_string()), limit, offset)
    print('QUERY get infected', query)
    res = None
    with get_connection().cursor() as cursor:
        cursor.execute(query)
        res = cursor.fetchall()
    close_connection()
    return res


def update_last_analysis_timestamp(device_ids, last_analysis_timestamp, debug=False):
    if debug:
        return True

    query = 'update infected_devices set last_analysis_timestamp = \'{}\' where device_id in ({})'\
        .format(last_analysis_timestamp.strftime(config.get_timestamp_format_string()), ','.join(device_ids))
    # print(query)
    with get_connection().cursor() as cursor:
        cursor.execute(query)
    get_connection().commit()
    close_connection()


if __name__ == "__main__":
    get_infected(datetime.now())
    # update_last_analysis_timestamp(['1', '2'], datetime.now())
