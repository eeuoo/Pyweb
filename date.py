from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta

dt = "2019-02-11 12:13:33"

d = dt.strftime('%Y-%m-%d %H/%M')

nichi = d + relativedelta(seconds=1)
now = datetime.now()

diff = now - nichi

if diff.days >= 1:
    print(d)

else :
    print(nichi)