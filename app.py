from flask import Flask
from models.Segment import Segment
from config.app import *

app = Flask(__name__)
app.config.from_object(Config)

from config.routes import *

app.register_blueprint(router)

if __name__ == '__main__':
    try:
        Segment.find_segment(0, 60)
        app.run()
    except KeyboardInterrupt:
        exit(0)
