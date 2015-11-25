# -*- coding: utf-8 -*-

# Django
from django.conf.urls import include, url

urlpatterns = [
	url(r'^$', 'portal.views.home_page', name = 'home'),
]
