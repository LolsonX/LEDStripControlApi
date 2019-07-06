from app import db
from models import Effect
from models.Color import Color
from models.Effect import Effect
from sqlalchemy.orm import sessionmaker

# red = Color(red=255, green=0, blue=0, name="red")
# green = Color(red=0, green=255, blue=0, name="green")
# blue = Color(red=0, green=0, blue=255, name="blue")
all_on = Effect(name="All leds on")
# db.session.add(red)
# db.session.add(green)
# db.session.add(blue)
db.session.add(all_on)
db.session.commit()

