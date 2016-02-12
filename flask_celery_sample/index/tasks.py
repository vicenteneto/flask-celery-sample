from flask_celery_sample.app_celery import celery


@celery.task
def hello():
    for i in range(10000):
        print 'Hello!'
