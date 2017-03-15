# -*- coding: utf-8 -*-

# Django
from django.conf.urls import include, url
from portal import views

urlpatterns = [
	url(r'^$', views.home_page, name = 'home'),
]
