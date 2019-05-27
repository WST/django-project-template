# -*- coding: utf-8 -*-
# Файл с настройками проекта

# Импортируем всё нужное
import os
import sys

# Конструировать пути можно таким образом: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# В продакшене это необходимо переопределить, например, через local_settings.py
SECRET_KEY = '{{ secret_key }}'

# Режим отладки. Исключительно для использования на машине разработчика.
DEBUG = True

# Разрешённые имена хоста. Рекомендуется определить в local_settings.py
ALLOWED_HOSTS = []

# Установленные в проекте Django-приложения
INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'bootstrap_pagination',
	'portal',
	'captcha',
]

# Задействованные middleware.
MIDDLEWARE = [
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'django.middleware.security.SecurityMiddleware',
	'portal.middleware.PortalMiddleware',
]

# Корневая карта URL-ок
ROOT_URLCONF = '{{ project_name }}.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
				'portal.context_processors.preprocess_context',
			],
		},
	},
]

# WSGI-приложение. Нет смысла трогать эту настройку, она установлена в единственно верное значение.
WSGI_APPLICATION = '{{ project_name }}.wsgi.application'

# Используемая БД
# http://djbook.ru/rel1.8/ref/databases.html
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'data.db'),
	}
}

# Языковые и региональные настройки
# http://djbook.ru/rel1.8/topics/i18n/index.html
LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = False
USE_L10N = True
USE_TZ = True


# Статические и медиа-файлы
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

try:
	from {{ project_name }}.local_settings import *
except:
	print("Failed to load local_settings.py")
	sys.exit(1)
