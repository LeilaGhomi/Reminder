from django import template
from django.utils import timezone
from apps.todo.models import Task

register = template.Library()


@register.simple_tag(name='re_time')
def remaining_time(task):
    re_t = task.schedule - timezone.now()
    return re_t


@register.inclusion_tag('recent_tasks.html')
def recent_tasks():
    tasks = Task.objects.all().order_by('-schedule')[:3]
    return {'tasks': tasks}


@register.filter
# @stringfilter
def capitalize(title):
    return title.title()
