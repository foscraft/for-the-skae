from flask import Flask
from skae_app.skaes.db import db_session
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_login import LoginManager
# from flask_bootstrap import Bootstrap
# from flask_moment import Moment
# from flask_mail import Mail
# from config import Config
from skae_app.skaes.views import skaes

app = Flask(__name__)
app.register_blueprint(skaes)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

