from flask import Flask, url_for, render_template, request, Response, session, jsonify, make_response, redirect
from datetime import timedelta, date, datetime
from helloflask.classes import Options, FormInput, Navi, Months
from helloflask import app
from helloflask.init_db import db_session
from helloflask.models import Singer, AlbumInfo, SongInfo, DailyList, MappingSS, User
from sqlalchemy.exc import SQLAlchemyError
from collections import namedtuple
from sqlalchemy.orm import subqueryload, joinedload


@app.route('/')
def main():
    date = '2019-01-25 14:45:51'
    mellist  = DailyList.query.filter_by(crawl_date = date).options(joinedload(DailyList.song))
    mellist = mellist.options(joinedload(DailyList.album))
    # ORM : DailyList - SongInfo - AlbumInfo 
    return render_template('meltop100.html', mellist=mellist)


@app.route('/songinfo/<song_id>')
def songinfo(song_id):
    
    song = SongInfo.query.filter_by(song_id = song_id).options(joinedload(SongInfo.album)).first()
    
 
    return render_template("songinfo.html", song=song)


@app.route('/mypage')
def mypage():
    return

@app.route('/login', methods=['GET'])
def login_get():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    passwd =  request.form.get('passwd')
    u = User.query.filter('email= :email and passwd = sha(:passwd, 256)').params(email=email, passwd=passwd).first()

    if u is not None:
        session['loginUserId'] = u.id
        session['loginUserName'] = u.nickname
        return redirect('/')
    else : 
        return render_template('login.html', email=email)

@app.route('/logout')
def logout():
    if session.get('loginUserId'):
        del session['loginUserId']
        del session['loginUserName']
    return redirect('/') 