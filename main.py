#coding=utf-8
from app import app
#Подключаем конфигурационный файл
from settings import Global_app_config
import views

if __name__ == '__main__':
    app.run()
