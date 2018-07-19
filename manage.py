from flask import Flask
from flask_script import Manager

from APP.views import blue
from APP.views2 import blue as blue2
app = Flask(__name__)

manager = Manager(app=app)

# 注册蓝图
app.register_blueprint(blueprint=blue)

app.register_blueprint(blueprint=blue2)

if __name__ == '__main__':
    # APP.run()
    manager.run()

