from datetime import datetime

def ymd(fmt):
    def trans(date_str):
        return datetime.strptime(date_str, fmt)
    return trans