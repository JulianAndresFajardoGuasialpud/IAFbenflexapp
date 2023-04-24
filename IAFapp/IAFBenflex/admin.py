from django.contrib import admin
from .models import Users
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("create_at",)
    
# Register your models here.
admin.site.register(Users),
admin.site.register(Task, TaskAdmin)