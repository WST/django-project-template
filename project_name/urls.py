# -*- coding: utf-8 -*-

# Внимание! Это глобальный urls.py проекта. Добавлять свои URL-ки лучше в urls.py приложения «portal».

# Django
from django.urls import include, path, re_path
from django.conf import settings
from django.contrib import admin
from django.views.static import serve as serve_static

# Наш проект
from portal import urls as portal_urls

urlpatterns = [
	path('admin/', admin.site.urls),
	path('captcha/', include('captcha.urls')),
	path('', include(portal_urls)),

	# Чисто отладочная строка
	re_path(r'^media/(?P<path>.*)$', serve_static, {'document_root': settings.MEDIA_ROOT}),
]
