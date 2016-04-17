from django.contrib import admin

from .models import Type, Style, Location, Restaurant, Menu

admin.site.register(Type)
admin.site.register(Style)
admin.site.register(Location)
admin.site.register(Restaurant)
admin.site.register(Menu)
# Register your models here.
