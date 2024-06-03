from django.contrib import admin
from home.models import service

class serviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')

admin.site.register(service, serviceAdmin)