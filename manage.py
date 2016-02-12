#!/usr/bin/env python
from flask_celery_sample.app import create_app
from flask.ext.script import Manager

manager = Manager(create_app())

if __name__ == '__main__':
    manager.run()
