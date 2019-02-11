# import sys; 
# print( sys.path)
from flask import Flask, g,  Response, make_response, request
from datetime import datetime, date


app = Flask(__name__)
app.debug = True


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


@app.route("/gg")
def helloworld():
    return "Hello World!" + getattr(g, 'str', '111')

@app.route("/")
def helloworld():
    return "Hello Flask World!!!!!"
