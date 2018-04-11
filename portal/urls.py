# -*- coding: utf-8 -*-

# Django
from django.urls import include, path
from portal import views

urlpatterns = [
	path('', views.home_page, name = 'home'),
]
