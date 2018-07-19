from manage import app


@app.route('/')
def index():
    return "Hello Flask"