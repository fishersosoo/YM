# -*- coding: utf-8 -*-
from app import db
from app.users import constants as USER
from flask_login import UserMixin
from collections import Counter

class YMDishComment(db.Model):
    __tablename__="ym_dish_comment"
    UserName=db.Column(db.String(20),db.ForeignKey('_user.UserName'),primary_key=True)
    DishID=db.Column(db.String(20),db.ForeignKey('ym_dish.DishID'),primary_key=True)
    Time=db.Column(db.DateTime)
    Content=db.Column(db.String(200))
    def __init__(self, UserName,DishID,Time,Content):
        self.UserName=UserName
        self.DishID=DishID
        self.Time=Time
        self.Content=Content

    def save(self):
        db.session.add(self)
        db.session.commit()
