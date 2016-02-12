from flask import Flask
from flask_celery_sample.index.views import blueprint


def create_app():
    app = Flask('flask_celery_sample')

    app.register_blueprint(blueprint)

    return app
