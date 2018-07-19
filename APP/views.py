from flask import Blueprint

blue = Blueprint('first_blue',__name__)

@blue.route('/')

def index():
    return "Hello Flask"