from django.urls import reverse, NoReverseMatch
from django.utils import timezone

from django.db import models

from apps.todo.manager import TaskManager, CategoryManager


class Category(models.Model):
    category_name = models.CharField(max_length=50)
    objects = CategoryManager()

    def __str__(self):
        return self.category_name


class Task(models.Model):
    PRIORITY = (
        ['1', 'top'],
        ['2', 'medium'],
        ['3', 'low']
    )

    title = models.CharField(max_length=100)
    notes = models.TextField()
    priority = models.CharField(choices=PRIORITY, null=True, max_length=1)
    schedule = models.DateTimeField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    done = models.BooleanField(default=False)

    objects = TaskManager()

    class Meta:
        ordering = ['schedule']

    def __str__(self):
        return self.title

    @property
    def task_maturity(self):
        try:
            maturity = self.schedule.day - timezone.now().day
        except AttributeError:
            maturity = 'unknown'
        return maturity

    # @property
    # def task_category(self):
    #     for c in self.CATEGORY:
    @property
    def remaining_time(self):
        re_t = self.schedule - timezone.now()
        return re_t

    def get_absolute_url(self):
        try:
            return reverse('task_detail', args=(str(self.id)))
        except NoReverseMatch:
            return reverse('404')