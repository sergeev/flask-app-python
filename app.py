# Входной и основной файл приложения
from flask import Flask
from config import Global_app_config

app = Flask(__name__)
app.config.from_object(Global_app_config)

@app.route('/')
def hello_world():
    return 'Hello, World!'
