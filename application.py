__author__ = 'sanledi.buli'

from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from controller import controller
from worker import *
import os
import atexit

application = Flask(__name__)
application.config.from_object(__name__)
application.secret_key = os.urandom(24)
application.debug = True
application.register_blueprint(controller)

scheduler = BackgroundScheduler()
scheduler.add_job(print_hello_world, 'interval', minutes=1, id='print_hello_world')
scheduler.start()

atexit.register(lambda: scheduler.shutdown(wait=False))

if __name__ == '__main__':
    print 'Hello Mas Andry... :D'
    application.run(host="0.0.0.0", port=7000, debug=True)