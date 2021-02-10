from django.contrib import admin
from frontend.models import *

# Register your models here.
admin.site.register(Property)
admin.site.register(Agents)
admin.site.register(Buy)
admin.site.register(Rent)
admin.site.site_header = 'Real Estate'
