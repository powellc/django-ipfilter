from django.contrib import admin 
from ipfilter.models import ExcludedIP

admin.site.register(ExcludedIP)
