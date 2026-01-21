import re
from datetime import datetime

def clean_text(text):
    return re.sub(r'\s+', ' ', text).strip()

def parse_date(date_str):
    try:
        return datetime.strptime(date_str, '%a, %d %b %Y %H:%M:%S %Z').strftime('%Y-%m-%d')
    except:
        return date_str

