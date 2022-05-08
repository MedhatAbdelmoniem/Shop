from flask import app
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from database.app.app import app
from database.model.model import db,setup_db

migrate = Migrate(app, db)
manager = Manager(app)
setup_db(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()