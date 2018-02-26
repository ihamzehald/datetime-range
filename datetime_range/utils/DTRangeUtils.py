"""
This module contains a set of helper methods to be used in datetime-range

"""

from datetime import datetime, timedelta

def is_valid_date_format(date):
    if type(date) is str:
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Incorrect date format, it should be YYYY-MM-DD")
    return True


def is_valid_date_type(date, param_name='date'):
    date_time_val = None
    if type(date) is str:
        date_time_val = datetime.strptime(date, "%Y-%m-%d")
    elif type(date) is datetime:
        date_time_val = date
    else:
        raise Exception(param_name + " type must be str or datetime object.")
    return date_time_val

