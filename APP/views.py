from flask import Blueprint, url_for, request, render_template, make_response, Response, redirect, abort
from flask.json import jsonify
from jinja2 import Template

blue = Blueprint('first_blue', __name__)


@blue.route('/')
def index():
    return "Hello Flask"


@blue.route('/hello/<int:a>')
def hello(a):
    print(a)
    print(type(a))

    return "这是一个hello!"


# 反向解析需要 + first_blue.xxx
@blue.route('/reverse/')
def reverse():
    # print(url_for('first_blue.hello',a=1))
    # print(url_for('first_blue.index'))
    print(url_for('second_blue.index'))

    return "反向解析需要注意的问题点！"


# request
# @blue.route('/request/')
@blue.route('/request/',methods=['GET','POST'])
def get_request():
    # print(request)
    # print(type(request))
    # print(request.path)
    # print(request.url)
    # print(request.data)
    # print(request.range)
    # print(request.values)
    # print(request.method)
    # print(request.form)
    # print(request.host)
    # print(request.user_agent)
    # print(request.remote_addr)
    # print(request.cookies)

    # print(request.args['name'])
    # print(request.args.get('name'))
    # http://127.0.0.1:5000/request/?name=laoli&name=laowang
    print(request.args.getlist('name'))

    # 反扒策略  状态码404
    return '这有个Request',404

@blue.route('/personinfo/')
def personinfo():

    # temp = render_template('PersonInfo.html')

    temp = Template('<h1>这是个模板{{user}}</h1>')
    print(temp)
    print(type(temp))
    # result = temp.render()
    result = temp.render(user = 'Tom')
    print(result)
    print(type(result))

    return "这有个模板",401

@blue.route('/makeresponse/')
def makeresponse():

    resp =  make_response("<h2>今天天气不错啊！</h2>",405)
    print(resp)
    print(type(resp))

    return resp

@blue.route('/response/')
def resp():

    resp = Response(response='<h2>人生苦短，我学Python！</h2>',status=404)

    return resp

# 请求重定向 redirect(url_for("xxx.xxx"))
@blue.route("/redirect/")
def redir():

    return redirect(url_for('first_blue.resp'))


# 终止abort
@blue.route('/hehe/')
def hehe():
    abort(404)

@blue.route('/json/')
def json():

    # data = {
    #     'name':'laoxu',
    #     'age':18,
    # }
    #
    # return jsonify(data)

    return jsonify(name='pangzi',age=18)


