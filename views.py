#coding=utf-8
from app import app
#Подключаем основной вид сайта
from flask import render_template

@app.route('/')
def index():
    #Тествая передача данных в шалон
    name = 'Test Data'
    return render_template('index/global.html', n = name)
