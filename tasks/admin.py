from django.contrib import admin

from guardian.admin import GuardedModelAdmin

from .models import Task


# Register your models here.
class TaskAdmin(GuardedModelAdmin):
    list_display = ('id', 'description', 'is_done', 'created')
    search_fields = ('description',)
    ordering = ('id',)


admin.site.register(Task, TaskAdmin)
