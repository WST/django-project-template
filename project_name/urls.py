# -*- coding: utf-8 -*-

# Django
from django.conf.urls import include, url
from django.contrib import admin

# Наш проект
from portal import urls as portal_urls

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'', include(portal_urls)),
]
