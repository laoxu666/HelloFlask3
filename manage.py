from flask import Flask
from flask_script import Manager

from APP.views import blue

app = Flask(__name__)

manager = Manager(app=app)

# 注册蓝图
app.register_blueprint(blueprint=blue)

if __name__ == '__main__':
    # APP.run()
    manager.run()

