# Домашняя работа №26. Шумихин Алексей 02.03.23
from flask import Flask
from app import create_app
from config import Config

app: Flask = create_app(Config)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=25000)
