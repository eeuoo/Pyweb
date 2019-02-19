from flask import Flask, g,  Response, make_response, request
from flask import Markup, session, render_template, url_for
from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta
import os
from helloflask import app
from helloflask.classes import Options, FormInput, Navi, Months
from helloflask.utils import ymd

from helloflask.init_db import db_session
from helloflask.models import User, AlbumInfo, SongInfo
from sqlalchemy.exc import SQLAlchemyError
from collections import namedtuple
from sqlalchemy.orm import subqueryload, joinedload




@app.route('/sql2')
def sql2():
    try : 
     ret = db_session.query(SongInfo).options(joinedload(SongInfo.album)).filter(SongInfo.likecnt < 10000)
    except SQLAlchemyError as sqlerr:
        db_session.rollback()
        print("SqlError>>", sqlerr)

    except:
        print("Error!!")

    finally : db_session.close()

    return render_template('main.html', ret=ret)

@app.route('/sql')
def idx():
    ret = 'OK'
    try:
        # Create(insert)
        u = User('abc@efg.com', 'hong')
        db_session.add(u)
        print("user.id=", u.id)
        
        # Read(select)1
        # u = User.query.filter(User.id == 1).first()
        # lst = User.query.all()

        # Read(select)2
        # s = db_session()
        # result = s.execute('select id, email, nickname from User where id > :id', {'id':1})
        # Record = namedtuple("User", result.keys())
        # rrr = result.fetchall()
        # print(">>", type(result), result.keys(), rrr)
        # records = [Record(*r) for r in rrr]

        # for r in records:
        #     print(r, r.nickname, type(r))

        # s.close()

        db_session.commit()

        # ret = User.query.all()
        
    except SQLAlchemyError as sqlerr:
        db_session.rollback()
        print("SqlError>>", sqlerr)

    except:
        print("Error!!")

    finally:
        db_session.close()

    # return "RET=" + str(ret)
    return render_template('main.html', userlist=ret)

@app.route('/ayear')
def ayear():
    monthlist = []
    today = '2019-02-14 09:22'
    year = datetime.today().year

    for m in range(1,13):
        monthlist.append(Months(year, m))

    return render_template('application.html', year=year, today=today, monthList=monthlist)

@app.route('/tryselect')
def tryselect():
    optionList = []
    for i in [1,2,3]:
        value = i
        text = 'selectTest' + str(i)
        optionList.append(Options( value, text))

    yesterday = "2019-02-13 15:22"
    today = "2019-02-14 13:24"
    tomorrow = "2019-02-15 11:11"

    return render_template('application.html', optionList=optionList, todayis=today, tomorrow=tomorrow, yesterday=yesterday)

@app.route('/macrotrythis')
def mcrtry():
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

# @app.route("/hello")
# def helloworld():
#     return "Hello Flask World!!!!!"