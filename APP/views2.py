from flask import Flask, Blueprint, url_for

blue = Blueprint("second_blue",__name__)

@blue.route('/abc/')
def index():
    return '这是第二个蓝图'
