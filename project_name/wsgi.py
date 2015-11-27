# -*- coding: utf-8 -*-

# WSGI-файл для развёртывания

# Системные импорты
import os

# Django
from django.core.wsgi import get_wsgi_application

# Задаём путь к модулю настроек
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_name.settings")

# Наш WSGI callable
application = get_wsgi_application()
