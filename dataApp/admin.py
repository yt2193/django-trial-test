from django.contrib import admin
from dataApp.models import Company
# Register your models here.
class Detailsview(admin.ModelAdmin):
    list_display=('name','age','address')
admin.site.register(Company,Detailsview)
