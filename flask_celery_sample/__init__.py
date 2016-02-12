# This will make sure the app is always imported when
# Flask starts so that shared_task will use this app.
from app_celery import celery as celery_app
