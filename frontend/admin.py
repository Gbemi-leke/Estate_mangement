from django.contrib import admin
from frontend.models import *

# Register your models here.
admin.site.register(Agents)
admin.site.register(AddProperty)
admin.site.site_header = 'Real Estate'
