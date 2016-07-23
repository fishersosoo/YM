# -*- coding: utf-8 -*-
from app import db,app
from app.users import constants as USER
from collections import Counter
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, BadSignature
from passlib.apps import custom_app_context as pwd_context

class User(db.Model):
    __tablename__='_user'
    UserName=db.Column(db.String(20),primary_key=True)
    Password=db.Column(db.String(128))
    HeadImage=db.Column(db.String(200))
    Email=db.Column(db.String(20))
    EmailVerified=db.Column(db.Boolean)
    MobilePhoneNumber=db.Column(db.String(100))
    MobilePhoneVerified=db.Column(db.Boolean)
    Hometown=db.Column(db.String(100))
    Gender=db.Column(db.Boolean)
    Birthday=db.Column(db.Date)
    Sentence=db.Column(db.String(140))
    NickName=db.Column(db.String(20))
    def __init__(self,UserName,Password,HeadImage,Email
                 ,EmailVerified,MobilePhoneNumber,MobilePhoneVerified
                 ,Hometown,Gender,Birthday,Sentence,NickName):
        self.UserName=UserName
        self.Password=pwd_context.encrypt(Password)
        self.HeadImage=HeadImage
        self.Email=Email
        self.EmailVerified=EmailVerified
        self.MobilePhoneNumber=MobilePhoneNumber
        self.MobilePhoneVerified=MobilePhoneVerified
        self.Hometown=Hometown
        self.Gender=Gender
        self.Birthday=Birthday
        self.Sentence=Sentence
        self.NickName=NickName

    def hash_password(self, password):
        self.Password = pwd_context.encrypt(password)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def generate_auth_token(self, expiration = 600):
        # create a token
        s = Serializer(app.config['SECRET_KEY'], expires_in = expiration)
        return s.dumps({ 'id': self.UserName })

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data=s.loads(token)
        except SignatureExpired:
             # valid token, but expired
            return None
        except BadSignature:
            # invalid token
            return None
        user = User.query.filter(User.UserName==data['id']).first()
        return user

    def verify_password(self, password):
        return self.Password == pwd_context.encrypt(password)


