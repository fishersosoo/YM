# -*- coding: utf-8 -*-
from app import db
from app.users import constants as USER
from flask_login import UserMixin
from collections import Counter


class YMDish(db.Model):
	__tablename='ym_dish'
	DishID=db.Column(db.String(20),primary_key=True)
	DishType=db.Column(db.String(10))
	DishSmallImage=db.Column(db.String(200))
	DishLargeImage=db.Column(db.String(200))
	DishName=db.Column(db.String(10))
	Taste=db.Column(db.String(20))
	RawStuff=db.Column(db.String(30))
	Locations=db.Column(db.String(20))
	Description=db.Column(db.String(400))
	Price=db.Column(db.Numeric(2))
	Like=db.Column(db.Integer)
	Favorite=db.Column(db.Integer)
	IsToday=db.Column(db.Boolean)
	def __init__(self,DishID,DishType,DishSmallImage
				 ,DishLargeImage,DishName,Taste
				 ,RawStuff,Locations,Description
				 ,Price,Like,Favorite,IsToday=False):
		 self.DishID=DishID
		 self.DishType=DishType
		 self.DishSmallImage=DishSmallImage
		 self.DishLargeImage=DishLargeImage
		 self.DishName=DishName
		 self.Taste=Taste
		 self.RawStuff=RawStuff
		 self.Locations=Locations
		 self.Description=Description
		 self.Price=Price
		 self.Like=Like
		 self.Favorite=Favorite
		 self.IsToday=IsToday

	def save(self):
		db.session.add(self)
		db.session.commit()

