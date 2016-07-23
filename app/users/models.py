# -*- coding: utf-8 -*-
from app import db
from app.users import constants as USER
from collections import Counter

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
        self.Password=Password
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

    def save(self):
        db.session.add(self)
        db.session.commit()

