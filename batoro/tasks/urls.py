from django.urls import path
from .views import (
    StatusListView,
    StatusCreateView,
    StatusUpdateView,
    delete_project_status,
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
)


app_name = "task"

urlpatterns = [
    # Status
    path("status", StatusListView.as_view(), name="status_list"),
    path("status/create/", StatusCreateView.as_view(), name="status_create"),
    path("status/update/<int:pk>/", StatusUpdateView.as_view(), name="status_update"),
    path("status/delete/<int:task_status_id>/", delete_project_status, name="status_delete"),
    # Tasks
    path("", TaskListView.as_view(), name="task_list"),
    path("create/", TaskCreateView.as_view(), name="task_create"),
    path("update/<int:pk>/", TaskUpdateView.as_view(), name="task_update"),
    # path("delete/<int:pk>/", delete_task_status.as_view(), name="task_delete"),
]
