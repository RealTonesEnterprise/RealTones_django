from django.contrib import admin
from .models import PersonalInfo, slider, brands_slider

# Register your models here.

admin.site.register(PersonalInfo)
admin.site.register(slider)
admin.site.register(brands_slider)
