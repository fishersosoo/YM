# -*- coding: utf-8 -*-
from app import app,db
from app.users import constants as USER
from collections import Counter
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, BadSignature
from passlib.apps import custom_app_context as pwd_context

class User(db.Model):
    __tablename__ = '_user'
    UserName = db.Column(db.String(20),primary_key = True)
    Password = db.Column(db.String(256))
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
    def __init__(self,UserName,Password,HeadImage,Email
                 ,EmailVerified,MobilePhoneNumber,MobilePhoneVerified
                 ,Hometown,Gender,Birthday,Sentence,NickName):
        self.UserName = UserName
        self.Password = Password
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

    def save(self):
        db.session.add(self)
        db.session.commit()


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

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return 'Token expired!'
            # valid token, but expired

        except BadSignature:
            return 'Signature Error!'
            # invalid token

        admin = Admin.query.filter(Admin.AdminName == data['id']).first()
        return admin

    def verify_password(self, password):
        return password==self.Password