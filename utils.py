import re
from datetime import datetime, timedelta


def generate_regex():
    # Generate date range (dates) from yesterday to today
    today = datetime.today()
    yesterday = datetime.today() - timedelta(days=1)
    regex_exp = re.compile(f".+[-\/]({today.year,yesterday.year})[-\/]({today.month,yesterday.month})[-\/]({today.day,yesterday.day})[-\/].*")
    return regex_exp

