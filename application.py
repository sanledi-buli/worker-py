__author__ = 'sanledi.buli'

from flask import Flask
from controller import controller
import os

application = Flask(__name__)
application.config.from_object(__name__)
application.secret_key = os.urandom(24)
application.debug = True
application.register_blueprint(controller)

if __name__ == '__main__':
    print 'Hello Mas Andry... :D'
    application.run(host="0.0.0.0", port=7000, debug=True)