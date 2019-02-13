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

class Options:
    def __init__(self, value, text=''):
        self.value = value
        self.text = text


@app.route('/tryselect')
def tryselect():
    optionList = []
    for i in [1,2,3]:
        value = i
        text = 'selectTest' + str(i)
        optionList.append(Options( value, text))

    return render_template('application.html', optionList=optionList)


class FormInput:
    def __init__(self, id='', name='', value='', checked='', text='', type='text'):
        self.id = id
        self.name = name
        self.value = value
        self.checked = checked
        self.text = text
        self.type = type

@app.route('/macrotrythis')
def idx():
    rds = []
    for i in [1,2,3]:
        id = 'r' + str(i)
        name = 'radiotest'
        value = i
        checked = ''
        if i == 2:
            checked = 'checked'
        text = 'RadioTest' + str(i)
        rds.append( FormInput(id, name, value, checked, text) )

    return render_template('application.html', ttt='TestTTT999', radioList=rds)

@app.route('/ttmacro')
def ttmacro():
    return render_template("application.html")

class Navi:
    def __init__(self, title, url='#', ref=[]):
        self.title = title
        self.url = url
        self.ref = ref

@app.route('/recursive')
def recursive():	

    py = Navi("파이썬","https://search.naver.com",[])
    java = Navi("자바","https://search.naver.com",[])
    prg =Navi("프로그래밍 언어","https://search.naver.com", [py, java])
    jinja = Navi("Jinja","https://search.naver.com",[])
    gc = Navi("Genshi, Cheetah","https://search.naver.com",[])
    flask = Navi("플라스크","https://search.naver.com",[jinja, gc])
    spr = Navi("스프링","https://search.naver.com",[])
    ndjs = Navi("노드JS","https://search.naver.com",[])
    webf = Navi("웹 프레임워크","https://search.naver.com",[flask,spr,ndjs])
    my = Navi("나의 일상","https://search.naver.com",[])
    issue = Navi("이슈 게시판","https://search.naver.com",[])
    others = Navi("기타","https://search.naver.com",[my, issue])

    return render_template("application.html", navis=[prg, webf, others])

@app.route('/meltop100')
def meltop():
    return render_template("meltop100.html")

@app.route('/tmpl2')
def t2():
    a = (1, "만남1", "김건모", False, [])
    b = (2, "만남2", "노사연", True, [a])
    c = (3, "만남3", "익명", False, [a,b])
    d = (4, "만남4", "익명", False, [a,b,c])

    return render_template("application.html", lst2=[a,b,c,d])


@app.route('/tmpl')
def t():
    title = Markup("<strong>title</strong>")
    mu = Markup("<h1>iii = <i>%s</i></h1>")
    h = mu % "Italic"
    lst = [ ("만남1", "김건모",False), ("만남2", "노사연",True), ("만남3", "김건삼",False), ("만남4", "노사사",True) ]

    return render_template('application.html', Title=title, mu=h, lst=lst)


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
