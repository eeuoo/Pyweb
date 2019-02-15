from flask import Flask
from flask import url_for, render_template
from datetime import timedelta, date, datetime
from helloflask.classes import Options, FormInput, Navi, Months
from helloflask import app
from helloflask.init_db import db_session
from helloflask.models import User

app = Flask("helloflask")     # __name__ : 파이썬이 실행될 때 __main__. module의 이름이 들어가야함.


@app.route('/')
def idx():
    try:
        # u = User('abc@efg.com', 'hong')
        # db_session.add(u)
        u = User.query.filter(User.id == 10).first()
        print("user.id=", u.id)
        db_session.delete(u)
        # u.email = 'indiflex1@gmail.com'
        # db_session.add(u)

        db_session.commit()

        ret = "aaa"
        # ret = User.query.all()
        ret = User.query.filter(User.id > 5)
        for user in ret:   # select * from Follower where user = 6
            user.followers = Follower.query.filter(user == user.id)
        
    except SQLAlchemyError as sqlerr:
        db_session.rollback()
        print("SqlError>>", sqlerr)

    except:
        print("Error!!")

    # return "RET=" + str(ret)
    return render_template('main.html', userlist=ret)