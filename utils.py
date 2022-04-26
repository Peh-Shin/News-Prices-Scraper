import re
from datetime import datetime, timedelta


def generate_regex():
    # Generate date range (dates) from yesterday to today
    today = datetime.today()
    yesterday = datetime.today() - timedelta(days=1)
    regex_exp = re.compile(
        f".+[-/]({str(today.year) + '|' + str(yesterday.year)})[-/]({'{:02d}'.format(today.month) + '|' + '{:02d}'.format(yesterday.month)})[-/]({str(today.day) + '|' + str(yesterday.day)})[-/].*"
    )
    return regex_exp
