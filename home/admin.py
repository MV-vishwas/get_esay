from django.contrib import admin
from home import models
# Register your models here.
admin.site.register(models.Member)
admin.site.register(models.Service)
admin.site.register(models.Service_provider)
