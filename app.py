#coding=utf-8
from flask import Flask
from settings import Global_app_config

app = Flask(__name__)
app.config.from_object(Global_app_config)
