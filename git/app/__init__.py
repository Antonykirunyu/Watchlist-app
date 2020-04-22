from flask import Flask, escape, request, views
from .config import DevConfig
app = Flask(__name__,instance_relative_config=True)

app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

from app import views

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'