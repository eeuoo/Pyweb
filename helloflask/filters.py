from helloflask.views import app
from datetime import datetime, date


# fiters

@app.template_filter('date')
def artist_names(likecnt):
    
    return 

@app.template_filter('ymd2')               
def datetime_ymd(dt, fmt='%Y%m%d'):
    dt = dt.strptime(fmt)
    dt = dt.strftime(dt, '%Y-%m-%d')
    return dt
    

@app.template_filter('ymd')               
def datetime_ymd(dt, fmt='%m-%d'):
    if isinstance(dt, date):
        return "<strong>%s</strong>" % dt.strftime(fmt)
    else:
        return dt


@app.template_filter('simpledate')
def simpledate(dt):
    if not isinstance(dt, date):
        dt = datetime.strptime(dt, '%Y-%m-%d %H:%M')

    if (datetime.now() - dt).days < 1:
        fmt = "%H:%M"
    else:
        fmt = "%m/%d"

    return "<strong>%s</strong>" % dt.strftime(fmt)
