from django import forms

from .models import Task, Category


class AddTaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'notes', 'category', 'priority', 'schedule', 'done']


class AddCategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name']
