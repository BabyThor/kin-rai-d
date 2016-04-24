from django.contrib import admin

from .models import Tag, Restaurant, Menu

admin.site.register(Tag)
admin.site.register(Restaurant)
admin.site.register(Menu)
# Register your models here.
