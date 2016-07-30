# -*- coding: utf-8 -*-
<<<<<<< HEAD
from app import db, app
=======
from app import app,db
>>>>>>> origin/manage
from app.users import constants as USER
from collections import Counter
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, BadSignature
from passlib.apps import custom_app_context as pwd_context
<<<<<<< HEAD


class User(db.Model):
    __tablename__ = '_user'
    UserName = db.Column(db.String(20), primary_key=True)
    Password = db.Column(db.String(128))
=======

class User(db.Model):
    __tablename__ = '_user'
    UserName = db.Column(db.String(20),primary_key = True)
    Password = db.Column(db.String(256))
>>>>>>> origin/manage
    HeadImage = db.Column(db.String(200))
    Email = db.Column(db.String(20))
    EmailVerified = db.Column(db.Boolean)
    MobilePhoneNumber = db.Column(db.String(100))
    MobilePhoneVerified = db.Column(db.Boolean)
    Hometown = db.Column(db.String(100))
    Gender = db.Column(db.Boolean)
    Birthday = db.Column(db.Date)
    Sentence = db.Column(db.String(140))
    NickName = db.Column(db.String(20))
<<<<<<< HEAD

    def __init__(self, UserName, Password, Email
                 , EmailVerified, MobilePhoneNumber, MobilePhoneVerified
                 , Hometown, Gender, Birthday, Sentence, NickName, HeadImage=''):
        self.UserName = UserName
        self.Password = pwd_context.encrypt(Password)
=======
    def __init__(self,UserName,Password,HeadImage,Email
                 ,EmailVerified,MobilePhoneNumber,MobilePhoneVerified
                 ,Hometown,Gender,Birthday,Sentence,NickName):
        self.UserName = UserName
        self.Password = Password
>>>>>>> origin/manage
        self.HeadImage = HeadImage
        self.Email = Email
        self.EmailVerified = EmailVerified
        self.MobilePhoneNumber = MobilePhoneNumber
        self.MobilePhoneVerified = MobilePhoneVerified
        self.Hometown = Hometown
        self.Gender = Gender
        self.Birthday = Birthday
        self.Sentence = Sentence
        self.NickName = NickName
<<<<<<< HEAD

    def hash_password(self, password):
        self.Password = pwd_context.encrypt(password)
=======
>>>>>>> origin/manage

    def save(self):
        db.session.add(self)
        db.session.commit()

<<<<<<< HEAD
    def generate_auth_token(self, expiration=600):
        # create a token
        s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': self.UserName})
=======

class Admin(db.Model):
    __tablename_  = "_admin"
    AdminName = db.Column(db.String(20),primary_key = True)
    Password = db.Column(db.String(256))

    def __init__(self, AdminName,Password):
        self.AdminName = AdminName
        self.Password = Password

    def save(self):
        db.session.add(self)
        db.session.commit()

    def generate_auth_token(self,expiration = 600):
        # create a token
        s = Serializer(app.config['SECRET_KEY'],expires_in = expiration)
        return s.dumps({'id':self.AdminName})
>>>>>>> origin/manage

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return 'Token expired!'
            # valid token, but expired

        except BadSignature:
<<<<<<< HEAD
            # invalid token
            return 'Signature Error!'

        user = User.query.filter(User.UserName == data['id']).first()
        return user

    def verify_password(self, password):
        return pwd_context.verify(password, self.Password)

    def change_password(self,old,new):
        if pwd_context.verify(old, self.Password):
            self.Password=pwd_context.encrypt(new)
            self.save()
            return True
        else:
            return False
=======
            return 'Signature Error!'
            # invalid token

        admin = Admin.query.filter(Admin.AdminName == data['id']).first()
        return admin

    def verify_password(self, password):
        return password==self.Password
>>>>>>> origin/manage
