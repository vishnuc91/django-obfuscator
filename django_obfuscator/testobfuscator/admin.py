from django.contrib import admin
from .models import *

# Register your models here.


class MymodelAdmin(admin.ModelAdmin):
    list_display = ['aname', 'date']
admin.site.register(MyModel, MymodelAdmin)
