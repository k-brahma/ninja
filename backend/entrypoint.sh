#!/bin/bash

# マイグレーションを実行
python manage.py makemigrations
python manage.py migrate

# サーバーを起動
exec python manage.py runserver 0.0.0.0:8000