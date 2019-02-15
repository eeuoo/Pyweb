from datetime import timedelta, date, datetime
from dateutil.relativedelta import relativedelta

class Months:
    def __init__(self, year, dayday):
        day = str(year)+"-" + str(dayday) + "-1"
        d = datetime.strptime(day, "%Y-%m-%d")
        self.startdt = (d.weekday() * -1) +1
        nextMonth = d + relativedelta(months=1)
        self.month = d.month
        self.enddt = (nextMonth - timedelta(1)).day +1


class Options:
    def __init__(self, value, text=''):
        self.value = value
        self.text = text

class FormInput:
    def __init__(self, id='', name='', value='', checked='', text='', type='text'):
        self.id = id
        self.name = name
        self.value = value
        self.checked = checked
        self.text = text
        self.type = type

class Navi:
    def __init__(self, title, url='#', ref=[]):
        self.title = title
        self.url = url
        self.ref = ref