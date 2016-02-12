from celery import Celery

from flask_celery_sample.settings import TASKS

# Initialize Celery
celery = Celery('flask_celery_sample.app_celery', broker='mongodb://localhost:27017/flask_celery_sample',
                include=TASKS)
