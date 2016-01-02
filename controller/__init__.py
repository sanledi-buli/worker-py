__author__ = 'sanledi.buli'

from flask import Blueprint

controller = Blueprint('controller',__name__)

@controller.route('/hello-world')
def hello_world():
    return 'Hello World API'