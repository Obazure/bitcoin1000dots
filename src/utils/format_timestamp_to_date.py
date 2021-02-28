from datetime import datetime


def format_timestamp_to_date(val):
    return datetime.fromtimestamp(int(val)).strftime("%d.%m.%y %H:%M:%S")
