#!/usr/bin/env python
from datetime import datetime, timedelta
from pprint import pprint
from utils.DTRangeUtils import *

class DatetimeRange:
    """
    A library to get a range from two dates

    __author__ = "Hamzeh al Darawsheh"
    __copyright__ = "Copyright 2018, datetime-range"
    __credits__ = ["Hamzeh al Darawsheh"]
    __license__ = "MIT"
    __version__ = "0.0.1"
    __maintainer__ = "Hamzeh al Darawsheh"
    __email__ = "ihamzehald@gmail.com"
    __status__ = "Development"
    """

    @staticmethod
    def get_date_range(start_date, end_date, is_string = False, start_date_included = True, end_date_included = True):
        """
        Get the date range between two dates
        :param start_date: str/datetime object in Y-m-d format as the start date of the date range
        :param end_date: str/datetime object in Y-m-d format as the end date of the date range
        :return: date_range as a dict that contains the start_date, end_date, days_count, days as date range
        Output sample:

        If is_string is False (default) the returned data will be in datetime objects form:

        {'days': [datetime.datetime(2018, 2, 20, 0, 0),
                  datetime.datetime(2018, 2, 21, 0, 0),
                  datetime.datetime(2018, 2, 22, 0, 0),
                  datetime.datetime(2018, 2, 23, 0, 0),
                  datetime.datetime(2018, 2, 24, 0, 0),
                  datetime.datetime(2018, 2, 25, 0, 0),
                  datetime.datetime(2018, 2, 26, 0, 0),
                  datetime.datetime(2018, 2, 27, 0, 0),
                  datetime.datetime(2018, 2, 28, 0, 0)],
         'days_count': 9,
         'end_date': datetime.datetime(2018, 2, 28, 0, 0),
         'start_date': datetime.datetime(2018, 2, 20, 0, 0)}

        If is_string True the returned data will be in str objects form:

        {'days': ['2018-02-20',
                  '2018-02-21',
                  '2018-02-22',
                  '2018-02-23',
                  '2018-02-24',
                  '2018-02-25',
                  '2018-02-26',
                  '2018-02-27',
                  '2018-02-28'],
         'days_count': 9,
         'end_date': '2018-02-28',
         'start_date': '2018-02-20'}


        If is_date_object is true the returned data will be all datetime objects

        """
        start_date_datetime = None
        end_date_datetime = None
        days_list = []
        days_count_result = 0
        date_range = {'start_date': '', 'end_date': '', 'days_count': '', 'days': []}

        is_valid_date(start_date)
        is_valid_date(end_date)

        if type(start_date) is str:
            start_date_datetime = datetime.strptime(start_date, "%Y-%m-%d")
        elif type(start_date) is datetime:
            start_date_datetime = start_date
        else:
            raise Exception("start_date must be str or datetime object.")

        if type(end_date) is str:
            end_date_datetime = datetime.strptime(end_date, "%Y-%m-%d")
        elif type(end_date) is datetime:
            end_date_datetime = end_date
        else:
            raise Exception("end_date must be str or datetime object.")

        if end_date_datetime < start_date_datetime:
            raise Exception("end_date must be greater than start_date.")

        days_difference_datetime = end_date_datetime - start_date_datetime

        days_count = days_difference_datetime.days

        for day_index in range(days_count + 1):

            if not start_date_included and day_index == 0:
                continue

            if not start_date_included and day_index == days_count:
                continue

            day = start_date_datetime + timedelta(day_index)
            if is_string:
                day = day.strftime("%Y-%m-%d")
            days_list.append(day)

        if is_string:
            start_date_datetime = start_date_datetime.strftime("%Y-%m-%d")
            end_date_datetime = end_date_datetime.strftime("%Y-%m-%d")

        days_count_result = len(days_list)

        date_range['start_date'] = start_date_datetime
        date_range['end_date'] = end_date_datetime
        date_range['days_count'] = days_count_result
        date_range['days'] = days_list

        return date_range

    def get_date_range_forward(date, days):
        return None

    def get_date_range_backword(date, days):
        return None

    def get_day_range(start_hour, end_hour):
        return None

    def get_day_hours(date):
        return None

    def get_day_minutes(date):
        return None

    def get_day_seconds(date):
        return None


