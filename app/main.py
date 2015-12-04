from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.pagedown import PageDown


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


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)