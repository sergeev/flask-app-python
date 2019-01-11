# Файл обработки запросов в приложении
from app import app
from config import Global_app_config

if __name__ == '__main__':
    app.run(debug=True)
