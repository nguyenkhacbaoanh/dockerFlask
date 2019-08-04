import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

# import model
from main.model import project

# import blueprints
from __init__ import blueprint

from main import create_app, db

app = create_app('dev')
app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.command
def run():
    app.run()

@manager.command
def test():
    """runs the unit test."""
    tests = unittest.TestLoader().discover('test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()