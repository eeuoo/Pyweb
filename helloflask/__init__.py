# import sys; 
# print( sys.path)
from flask import Flask, g,  Response, make_response, request
from flask import Markup, session, render_template
from datetime import datetime, date, timedelta

app = Flask(__name__)
app.debug = True
app.config.update(
	SECRET_KEY='X1243yRH!mMwf',
	SESSION_COOKIE_NAME='pyweb_flask_session',
	PERMANENT_SESSION_LIFETIME=timedelta(31)      # 31 days
)

@app.route('/tmpl')
def t():
    title = Markup("<strong>title</strong>")
    mu = Markup("<h1>iii = <i>%s</i></h1>")
    h = mu % "Italic"
    print("h=", h)

    return render_template('application.html', Title=title, mu=h)


@app.route('/setsession')
def setSess():
    session['Token'] = '123X'
    return "Session이 설정되었습니다!"

@app.route('/getsession')
def getSess():
    return session.get('Token')

@app.route('/wc')
def writeCookie():
    res = Response("SET COOKIE / SESSION")
    k = request.args.get('key')
    v = request.args.get('val')
    res.set_cookie(k,v)

    return make_response(res)

@app.route('/rc')
def readCookie():
    k = request.args.get('key')
    v = request.cookies.get(k)
    return "Cookie['" + k + "'] =" + v   

@app.route('/resenv')
def reseniv():
    print("is_xhr : ", request.is_xhr)
    print("endpoint : ",request.endpoint)
    print("max_content_lenght : ",request.max_content_length)

    return ('REQUEST_METHOD: %(REQUEST_METHOD)s <br>'
        'SCRIPT_NAME: %(SCRIPT_NAME)s <br>'
        'PATH_INFO: %(PATH_INFO)s <br>'
        'QUERY_STRING: %(QUERY_STRING)s <br>'
        'SERVER_NAME: %(SERVER_NAME)s <br>'
        'SERVER_PORT: %(SERVER_PORT)s <br>'
        'SERVER_PROTOCOL: %(SERVER_PROTOCOL)s <br>'
        'wsgi.version: %(wsgi.version)s <br>'
        'wsgi.url_scheme: %(wsgi.url_scheme)s <br>'
        'wsgi.input: %(wsgi.input)s <br>'
        'wsgi.errors: %(wsgi.errors)s <br>'
        'wsgi.multithread: %(wsgi.multithread)s <br>'
        'wsgi.multiprocess: %(wsgi.multiprocess)s <br>'
        'wsgi.run_once: %(wsgi.run_once)s') % request.environ


def ymd(fmt):
    def trans(date_str):
        return datetime.strptime(date_str, fmt)
    return trans

@app.route('/dt')
def dt():
    datestr = request.values.get('date', date.today(), type=ymd('%Y-%m-%d'))
    return "우리나라 시간 형식: " + str(datestr)

@app.route('/test/<tid>')
def test3(tid):
	print("tid is", tid)

@app.route('/test_wsgi')
def wsgi_test():
    def application(environ, start_response):
        body = 'The request method was %s' % environ['REQUEST_METHOD']
        headers = [ ('Content-Type', 'text/plain'), 
					('Content-Length', str(len(body))) ]
        start_response('200 OK', headers)
        return [body]

    return make_response(application)

@app.route('/res1')
def res1():
    custom_res = Response("Custom Response", 200, {'test': 'ttt'})
    return make_response(custom_res)


# @app.before_request
# def before_request():
#     print("before_request!!!")


# @app.route("/gg")
# def helloworld():
#     return "Hello World!" + getattr(g, 'str', '111')

# @app.route("/")
# def helloworld():
#     return "Hello Flask World!!!!!"
