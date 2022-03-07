from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user
import numpy as np
import joblib
from .models import UserPred
from . import db
from sklearn.preprocessing import LabelEncoder


main = Blueprint('main', __name__)

model = joblib.load('appartment_price_prediction_model.sav')
lbl_encoder = joblib.load('dict_label.pkl')


@main.route('/')
def home():
	return render_template('index.html')


@main.route('/index.html')
def home_sir():
	return render_template('index.html')


@main.route('/profile.html')
@login_required
def profile():
	predictions = UserPred.query.order_by(UserPred.pred).all()
	return render_template('profile.html', predictions=predictions, name=current_user.name)


@main.route('/delete/<int:id>')
def delete(id):
	pred_to_delete = UserPred.query.get_or_404(id)
	db.session.delete(pred_to_delete)
	db.session.commit()
	return redirect(url_for('main.profile'))


@main.route('/predict.html')
@login_required
def prediction():
	return render_template('predict.html')


@main.route('/map.html')
def map():
	return render_template('map.html')


@main.route('/prediction-made',methods=['POST', 'GET'])
def prediction_made():

	int_features = [int(item) for item in request.form.values()]
	print(int_features)

	prediction = model.predict([int_features])
	answer = prediction[0]
	nrcamere = request.form.get('Nr. camere')
	suprconstr = request.form.get('Suprafata construita')
	anconstructie = request.form.get('An constructie')

	new_lst = [int_features[indx] for indx in range(2, len(int_features))]
	new_lst.pop(2)

	indx = 0
	hopefully_last_list = list()

	for value in lbl_encoder.values():
		hopefully_last_list.extend(value.inverse_transform([new_lst[indx]]))
		indx += 1
	
	new_answer = UserPred(pred=int(answer), nrcamere=nrcamere, suprconstr=suprconstr, 
		etaj=hopefully_last_list[0], nrbai=hopefully_last_list[1], anconstructie=anconstructie, nrbalcoane=hopefully_last_list[2],
		zona=hopefully_last_list[3], finorinconstr=hopefully_last_list[4], balinchisordeschis=hopefully_last_list[5])

	db.session.add(new_answer)
	db.session.commit()

	return render_template('predict.html', pred='Pretul prezis este de {0} €.'.format((str(int(answer)))))
	