from django.contrib import admin
from .models import Task
# Register your models here.


class TaskaAdmin(admin.ModelAdmin):
    readonly_fields = ("created", )


admin.site.register(Task, TaskaAdmin)
