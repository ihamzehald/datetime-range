from datetime import datetime, timedelta

def is_valid_date(date):
    if type(date) is str:
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Incorrect date format, it should be YYYY-MM-DD")
    return True