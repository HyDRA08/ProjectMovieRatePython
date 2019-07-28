from django.contrib import admin
from .models import modelsignup,modelmovie,modelrating

# Register your models here.

admin.site.register(modelsignup)
admin.site.register(modelmovie)
admin.site.register(modelrating)