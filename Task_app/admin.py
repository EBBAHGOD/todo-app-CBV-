from django.contrib import admin
from . import models
# Register your models here.


class taskview(admin.ModelAdmin):
    list_display=['task_name','user','task_date']
    list_filter = ['user']

admin.site.register(models.Task_list,taskview)