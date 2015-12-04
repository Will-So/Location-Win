from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.pagedown import PageDown
from app.forms import BusinessForm
import os


bootstrap = Bootstrap()
pagedown = PageDown()


db = SQLAlchemy()

## Will proabably want to login later
# login_manager = LoginManager()
# login_manager.session_protection = 'strong'
# login_manager.login_view = 'auth.login'

app = Flask(__name__)
bootstrap.init_app(app)
pagedown.init_app(app)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'hard to guess string'


@app.route('/')
def index():
    form = BusinessForm()
    if form.validate_on_submit():
        # TODO: Validation logic here
        pass

    return render_template('index.html', form=form)


@app.route('/best_location')
def best_location():
    return render_template('best_location.html')

if __name__ == '__main__':
    app.run(debug=True)