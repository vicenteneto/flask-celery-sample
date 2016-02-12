from celery import Celery

from flask_celery_sample import settings

# Initialize Celery
celery = Celery('flask_celery_sample.app_celery', broker='mongodb://localhost:27017/flask_celery_sample')
celery.autodiscover_tasks(lambda: settings.PACKAGES)
