from flask import Flask
from flask_babel import Babel
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event
from sqlalchemy.engine import Engine

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
babel = Babel(app)


# Activate Sqlite Foreign key constraint
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
  cursor = dbapi_connection.cursor()
  cursor.execute("PRAGMA foreign_keys=ON")
  cursor.close()

# from . import views
# from . import models
# from . import jinja_custom_filter
