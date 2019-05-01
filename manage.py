# https://flask-migrate.readthedocs.io/en/latest/
# https://github.com/miguelgrinberg/Flask-Migrate
# migrating database from 1 version to another
# usage
# $ python manage.py db [commands]
# for help use
# $ python manage.py db

from app.__init__ import db, app
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

manager.run()
