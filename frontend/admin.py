from django.contrib import admin
from frontend.models import *

# Register your models here.
admin.site.register(Sponsored)
admin.site.register(Latest)
admin.site.register(Featured)
admin.site.site_header = 'Real Estate'
