#!/usr/bin/env python
from datetime import datetime, timedelta
from pprint import pprint
from utils.DTRangeUtils import *

class DatetimeRange:
    """
    A library to get a range from a date

    __author__ = "Hamzeh al Darawsheh"
    __copyright__ = "Copyright 2018, Hamzeh al Darawsheh"
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

        is_valid_date_format(start_date)
        is_valid_date_format(end_date)
        start_date_datetime = is_valid_date_type(start_date, 'start_date')
        end_date_datetime = is_valid_date_type(end_date, 'end_date')

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

    @staticmethod
    def get_date_range_forward(date, days, is_string=False, start_date_included=False):
        """
        Get the date range of the next x days from date
        :param date: str/datetime object as the start date to get the next x days range
        :param days: int as the number of the days in the future that you want to get it's date range
        :param is_string: bool as the type of the returned data, True will return the data in string form
        :param start_date_included: bool weather the start date included in the returned range set or not
        :return:date_range as a dict that contains the date range of the next x days
        Output sample:

        If  is_string is False (default) the returned data will be in datetime objects form:

            {'days': ['2018-02-06',
                      '2018-02-07',
                      '2018-02-08',
                      '2018-02-09',
                      '2018-02-10',
                      '2018-02-11',
                      '2018-02-12'],
             'days_count': 7,
             'end_date': '2018-02-12',
             'start_date': datetime.datetime(2018, 2, 6, 0, 0)}

        If is_string True the returned data will be in str objects form:

            {'days': [datetime.datetime(2018, 2, 6, 0, 0),
                      datetime.datetime(2018, 2, 7, 0, 0),
                      datetime.datetime(2018, 2, 8, 0, 0),
                      datetime.datetime(2018, 2, 9, 0, 0),
                      datetime.datetime(2018, 2, 10, 0, 0),
                      datetime.datetime(2018, 2, 11, 0, 0),
                      datetime.datetime(2018, 2, 12, 0, 0)],
             'days_count': 7,
             'end_date': datetime.datetime(2018, 2, 12, 0, 0),
             'start_date': datetime.datetime(2018, 2, 6, 0, 0)}

        """
        if not type(days) is int:
            raise Exception("days param should be a valid integer.")

        is_valid_date_format(date)

        date = is_valid_date_type(date)

        start_date = date
        days_list = []
        date_range = {'start_date': '', 'end_date': '', 'days_count': '', 'days': []}

        for day_index in range(days + 1):

            if not start_date_included and day_index == 0:
                start_date = date + timedelta(1)
                continue

            day = date + timedelta(day_index)

            if is_string:
                day = day.strftime("%Y-%m-%d")

            days_list.append(day)


        date_range['start_date'] = start_date
        date_range['end_date'] = days_list[len(days_list)-1]
        date_range['days_count'] = len(days_list)
        date_range['days'] = days_list


        return date_range

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


