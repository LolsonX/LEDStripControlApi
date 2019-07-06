from flask import Flask
from flask_migrate import Migrate

from config.app import *
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

import migrations
migrate = Migrate(app, db)

from config.routes import *
app.register_blueprint(router)

if __name__ == '__main__':
    app.run()
