# -*- coding: utf-8 -*-

# компоненты Django
from django.http import HttpResponse, HttpResponseForbidden, Http404
from django.template import RequestContext
from django.shortcuts import render_to_response as render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods, require_POST, require_GET
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.urls import reverse
from django.db.models import Q
from django.db import connection

# наш проект
from portal.models import *
from portal.forms import *
from portal.utils import *

# Обработчик главной страницы сайта
def home_page(request):
	return render('home-page.htt', {'seo': seo_data('home')}, RequestContext(request))
