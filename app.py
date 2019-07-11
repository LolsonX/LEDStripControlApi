import time

from flask import Flask
from flask_migrate import Migrate
from services.ScriptThread import ScriptThread
from config.app import *
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
script_thread = ScriptThread()

migrate = Migrate(app, db)

from config.routes import *
app.register_blueprint(router)

if __name__ == '__main__':
    try:
        app.run()
    except KeyboardInterrupt:
        script_thread.stop()
        exit(0)
