from flask import Flask, render_template, request, jsonify
from flask.ext.bootstrap import Bootstrap
from app.forms import BusinessForm
import pandas as pd
import os


bootstrap = Bootstrap()
app = Flask(__name__)
bootstrap.init_app(app)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'hard to guess string'


@app.route('/', methods=('POST', 'GET'))
def index():
    form = BusinessForm()
    # if form.validate_on_submit():
    #     vect = input_to_vector(form)
    #     prediction = predict_success(vect)



    return render_template('index.html', form=form)


@app.route('/_handle_prediciton')
def _handle_prediction():
    """
    Takes input of categories and returns the chances of success client-side.
    :return:
    """
    loc = request.args.get('loc', 0, type=list)
    vect = input_to_vector(loc)
    prediction = predict_success(vect)

    return jsonify(prediction=prediction)

@app.route('/best_location')
def best_location():
    return render_template('best_location.html')


@app.route('/predictor')
def predictor():
    return render_template('predictor.html')

if __name__ == '__main__':
    app.run(debug=True)


def input_to_vector(form, location):
    """
    Takes input coordinates and two categories returns
    :param form:
    :return:
    """
    df = pd.DataFrame()
    df['city'] = form.city
    df['cat_1'] = form.business
    df['cat_2'] = form.additional_category

def predict_success(vect):
    """
    Predicts the success of a
    :param vect:
    :return:
    """