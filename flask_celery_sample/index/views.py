from flask import Blueprint
from flask_celery_sample.index.tasks import hello

blueprint = Blueprint('index', __name__)


@blueprint.route('/')
def index():
    hello.delay()
    return 'It works!'
