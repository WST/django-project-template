# -*- coding: utf-8 -*-

# Django
from django.core.management.base import BaseCommand, CommandError
from django.db import models

# наш project
from portal.models import *

class Command(BaseCommand):
	args = None
	help = 'A dummy example command with an abstract name'
	db = None

	def handle(self, *args, **options):
		self.stdout.write(u'Команда отработала успешно')
