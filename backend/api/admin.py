"""Модуль административной панели для приложения API."""


from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """Класс настройки административного интерфейса для задач."""

    list_display = ('title', 'description', 'completed')


admin.site.register(Task, TaskAdmin)
