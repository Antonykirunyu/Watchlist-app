from flask import Flask, escape, request, views
from .config import DevConfig
from flask_bootstrap import Bootstrap
from app import error
from app import views
app = Flask(__name__,instance_relative_config=True)

app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

bootstrap = Bootstrap(app)

from app import views

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'