from flask import Flask
from app.extensions import db, migrate
import os


def create_app():

    app = Flask(__name__)

    settings = os.environ['APP_SETTINGS']

    app.config.from_object(settings)

    db.init_app(app)
    migrate.init_app(app, db, command='db')

    from app import model

    from app.api import access

    app.register_blueprint(access, url_prefix='/api/access')


    @app.route('/test')
    def test():
        return {'status': 'success'}

    return app
