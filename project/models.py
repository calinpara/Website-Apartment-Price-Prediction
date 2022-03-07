from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(100), unique=True)
	password = db.Column(db.String(100))
	name = db.Column(db.String(1000))


class UserPred(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	pred = db.Column(db.String(100))
	nrcamere = db.Column(db.String(100))
	suprconstr = db.Column(db.String(100))
	etaj = db.Column(db.String(100))
	nrbai = db.Column(db.String(100))
	anconstructie = db.Column(db.String(100))
	nrbalcoane = db.Column(db.String(100))
	zona = db.Column(db.String(100))
	finorinconstr = db.Column(db.String(100))
	balinchisordeschis = db.Column(db.String(100))
	


	

