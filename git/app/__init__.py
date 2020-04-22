from flask import Flask, escape, request, views
from .config import DevConfig
from flask_bootstrap import Bootstrap
from app import error
from app import views
from flask import Flask
from config import config_options
app = Flask(__name__,instance_relative_config=True)

app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')
app.config.from_object(config_options[config_name])

bootstrap = Bootstrap(app)
bootstrap.init_app(app)

    return app

from app import views

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'