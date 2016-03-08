# -*- coding: utf-8 -*-

# Наш проект
from portal.models import *

# Запросить SEO-данные для страницы
def seo_data(page_slug):
	try:
		data = SEOData.objects.get(position = position)
		return data
	except:
		return {}

# Проанализировать запрос и извлечь из него номер запрошенной страницы (для постраничного вывода)
def get_page_number(request):
	try:
		page = int(request.GET.get('page', '0'))
		if page <= 0:
			return 1
	except:
		return 1

	return page
