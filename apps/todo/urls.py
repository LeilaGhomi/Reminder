from django.urls import path

from .views import TaskList, TaskDetail, CategoryList, AddTaskView, CategoryDetail, expired_tasks, TaskUpdate, download_tasks, AddCategoryView

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('<int:pk>', TaskDetail.as_view(), name='task_detail'),
    path('category/', CategoryList.as_view(), name='task_category'),
    path('add/', AddTaskView.as_view(), name='add_new_task'),
    path('add_category/', AddCategoryView.as_view(), name='add_new_category'),
    path('category/<int:pk>', CategoryDetail.as_view(), name='category_detail'),
    path('expired/', expired_tasks, name='expired_tasks'),
    # path('download/', download_tasks, name='download_tasks'),
    path('<int:pk>/update/', TaskUpdate.as_view(), name='update_task'),

]
