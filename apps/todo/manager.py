from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.utils import timezone


class TaskManager(models.Manager):
    def get_task(self, **extra_field):
        try:
            return self.get(**extra_field)
        except ObjectDoesNotExist:
            print('this object dose not exist')

    def expired_tasks(self):
        qs = self.get_queryset()
        expired_task = []
        for task in qs:
            if task.schedule < timezone.now() and task.done != True:
                expired_task.append(task)
        return expired_task
        # return qs.filter(qs.schedule < timezone.now(), qs.done != True)


class CategoryManager(models.Manager):
    def category_with_no_task(self):
        qs = self.get_queryset()
        categories = []
        for category in qs:
            if not category.task_set.all():
                categories.append(category)
        return categories
