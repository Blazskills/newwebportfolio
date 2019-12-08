

from run import db,app
from datetime import datetime
from flask_login import LoginManager,UserMixin,login_user, logout_user, login_required,current_user

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view ='login'


@login_manager.user_loader
def load_user(user_id):
       return Regtb.query.filter_by(id=user_id).first()

class Regtb(db.Model,UserMixin):
       id = db.Column(db.Integer,primary_key=True)
       name = db.Column(db.String(255))
       username = db.Column(db.String(255))
       career = db.Column(db.String(255))
       email = db.Column(db.String, unique=True, nullable=False)
       password = db.Column(db.String(255))
       phone = db.Column(db.Integer)
       userpix = db.Column(db.String(200))
       Reg_Date=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)




class Biotb(db.Model,UserMixin):
       id = db.Column(db.Integer,primary_key=True)
       aboutcontent = db.Column(db.Text)
       whycontent = db.Column(db.Text)
       visioncontent = db.Column(db.Text)
       career1 = db.Column(db.String(255))
       career2 = db.Column(db.String(255))
       career3 = db.Column(db.String(255))
       fblk = db.Column(db.String(255))
       twlk = db.Column(db.String(255))
       gitlk = db.Column(db.String(255))
       linkedinlk = db.Column(db.String(255))
       anylk = db.Column(db.String(255))
       userpix =db.Column(db.String(200))
       today=db.Column(db.Date, nullable=False, default=datetime.now)

class servicetb(db.Model,UserMixin):
       id = db.Column(db.Integer,primary_key=True)
       headings = db.Column(db.String(55))
       servicecontent = db.Column(db.Text)
       today=db.Column(db.Date, nullable=False, default=datetime.now)


class portfoliotb(db.Model,UserMixin):
       id = db.Column(db.Integer,primary_key=True)
       portfoliocontent = db.Column(db.Text)
       portfoliotitle = db.Column(db.String(255))
       clientname = db.Column(db.String(255))
       portcategory = db.Column(db.String(255))
       portwebname = db.Column(db.String(255))
       dod = db.Column(db.String(255))
       portpix =db.Column(db.String(200))
       today=db.Column(db.Date, nullable=False, default=datetime.now)

class testimonytb(db.Model,UserMixin):
       id = db.Column(db.Integer,primary_key=True)
       name = db.Column(db.String(255))
       testcontent = db.Column(db.Text)
       jobdescription = db.Column(db.String(255))
       testpix =db.Column(db.String(200))
       today=db.Column(db.Date, nullable=False, default=datetime.now)

class blogtb(db.Model,UserMixin):
       id = db.Column(db.Integer,primary_key=True)
       blogcontent = db.Column(db.Text)
       title = db.Column(db.String(255))
       name = db.Column(db.String(255))
       totalview = db.Column(db.BigInteger,default=0)
       likes = db.Column(db.BigInteger,default=0)
       blogpix =db.Column(db.String(200))
       today=db.Column(db.Date, nullable=False, default=datetime.now)

class contacttb(db.Model,UserMixin):
       id = db.Column(db.Integer,primary_key=True)
       number1 = db.Column(db.Integer)
       number2 = db.Column(db.Integer)
       mail1 = db.Column(db.String(255))
       mail2 = db.Column(db.String(255))
       location1 = db.Column(db.String(255))
       location2 = db.Column(db.String(255))
       today=db.Column(db.Date, nullable=False, default=datetime.now)


class contactmsgtb(db.Model,UserMixin):
       id = db.Column(db.Integer,primary_key=True)
       name = db.Column(db.String(255))
       email = db.Column(db.String(255))
       message = db.Column(db.String(255))
       today=db.Column(db.Date, nullable=False, default=datetime.now)

class sponsortb(db.Model,UserMixin):
       id = db.Column(db.Integer,primary_key=True)
       sponsorpix =db.Column(db.String(200))
       today=db.Column(db.Date, nullable=False, default=datetime.now)

class mailtb(db.Model,UserMixin):
       id = db.Column(db.Integer,primary_key=True)
       mails = db.Column(db.String(255))
       today=db.Column(db.Date, nullable=False, default=datetime.now)

