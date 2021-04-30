from django.contrib import admin

from apps.todo.models import Task, Category


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'notes', 'priority', 'schedule']
    list_filter = ['category']
    search_fields = ['task_maturity']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'id']
