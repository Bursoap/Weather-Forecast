import os

from flask import Flask
from dotenv import load_dotenv
from flask_migrate import MigrateCommand, Migrate
from flask_script import Manager, Server

from managers import DatabaseManager
from managers.application import ApplicationManager

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__name__), '.env'))


def create_app(app_name):
    import settings  # noqa
    app = Flask(app_name)
    os.environ['APPS_DIR'] = os.path.join(os.path.dirname(__name__), 'apps')
    config_obj = os.environ.get('APP_SETTINGS', settings.LocalConfig)
    app.config.from_object(config_obj)
    return app


app = create_app('Weather Forecast')
db = DatabaseManager.setup_db(app)

ApplicationManager.register_applications(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server(host=app.config['HOST'],
                                        port=app.config['PORT']))

if __name__ == '__main__':
    manager.run()
