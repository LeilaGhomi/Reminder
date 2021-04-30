from django.core.serializers import serialize
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from rest_framework.views import APIView
from django.views.generic.edit import UpdateView
from .forms import AddTaskModelForm, AddCategoryModelForm
from .models import Task, Category
from .serializers import TaskModelSerializer
from rest_framework import serializers


class TaskList(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'task_list'


# class TaskDetail(DetailView):
#     model = Task
#     template_name = 'task_detail.html'


class TaskDetail(UpdateView):
    model = Task
    template_name = 'task_detail.html'
    fields = ['title', 'notes', 'category', 'priority', 'schedule', 'done']


# class CategoryList(ListView):
#     model = Category
#     template_name = 'task_category.html'
#     context_object_name = 'categories_list'

class CategoryList(View):
    def get(self, request):
        categories = Category.objects.all()
        cat_with_no_task = Category.objects.category_with_no_task()
        return render(request, 'task_category.html', {'categories': categories, 'cat_with_no_task': cat_with_no_task})


class CategoryDetail(DetailView):
    model = Category
    template_name = 'category_detail.html'


class AddTaskView(View):
    def get(self, request):
        form = AddTaskModelForm()
        return render(request, 'add_task.html', {'form': form})

    def post(self, request):
        form = AddTaskModelForm(request.POST)
        if form.is_valid():
            validated_data = form.cleaned_data
            obj = Task(**validated_data)
            obj.save()
            return redirect('ok')
        return render(request, 'add_task.html', {'form': form})


def expired_tasks(request):
    tasks = Task.objects.expired_tasks()
    return render(request, 'expired_tasks.html', {'tasks': tasks})


# class TaskAll(APIView):
#     def get(self, request):
#         obj = Task.objects.all()
#         serialized = TaskModelSerializer(obj, many=True)
#         return JsonResponse(serialized.data, safe=False)
#


def download_tasks():
    serialized_tasks = serialize('json', Task.objects.all(),
                                 fields=['title', 'notes', 'category', 'priority', 'schedule', 'done'])
    with open('task_list.txt', 'w') as f:
        f.write(serialized_tasks)


class TaskUpdate(UpdateView):
    model = Task
    fields = ['done']
    template_name = 'update_task.html'


class AddCategoryView(View):
    def get(self, request):
        form = AddCategoryModelForm()
        return render(request, 'add_category.html', {'form': form})

    def post(self, request):
        form = AddCategoryModelForm(request.POST)
        if form.is_valid():
            validated_data = form.cleaned_data
            obj = Category(**validated_data)
            obj.save()
            return redirect('ok')
        return render(request, 'add_category.html', {'form': form})
