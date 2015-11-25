# -*- coding: utf-8 -*-

from django.db import models, connection
from django.utils import timezone
from django.forms import ValidationError
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.db.models.signals import post_save

