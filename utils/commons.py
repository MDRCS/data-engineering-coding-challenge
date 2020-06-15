from datetime import datetime


class Utils(object):

    @staticmethod
    def sec_to_date(sec_date):
        return datetime.fromtimestamp(sec_date).strftime("%A, %B %d, %Y %I:%M:%S")

