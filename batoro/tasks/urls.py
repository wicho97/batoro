from django.urls import path
from .views import (
    StatusListView,
    StatusCreateView,
    StatusUpdateView,
    delete_task_status,
    PriorityListView,
    PriorityCreateView,
    PriorityUpdateView,
    delete_task_priority,
    TypeListView,
    TypeCreateView,
    TypeUpdateView,
    delete_task_type,
    # TaskListView,
    # TaskCreateView,
    # TaskUpdateView,
)


app_name = "task"

urlpatterns = [
    # Status
    path("status", StatusListView.as_view(), name="status_list"),
    path("status/create/", StatusCreateView.as_view(), name="status_create"),
    path("status/update/<int:pk>/", StatusUpdateView.as_view(), name="status_update"),
    path(
        "status/delete/<int:task_status_id>/", delete_task_status, name="status_delete"
    ),
    # Priority
    path("priority", PriorityListView.as_view(), name="priority_list"),
    path("priority/create/", PriorityCreateView.as_view(), name="priority_create"),
    path(
        "priority/update/<int:pk>/",
        PriorityUpdateView.as_view(),
        name="priority_update",
    ),
    path(
        "priority/delete/<int:task_priority_id>/",
        delete_task_priority,
        name="priority_delete",
    ),
    # Type
    path("type", TypeListView.as_view(), name="type_list"),
    path("type/create/", TypeCreateView.as_view(), name="type_create"),
    path("type/update/<int:pk>/", TypeUpdateView.as_view(), name="type_update"),
    path("type/delete/<int:task_type_id>/", delete_task_type, name="type_delete"),
    # Tasks
    # path("", TaskListView.as_view(), name="task_list"),
    # path("create/", TaskCreateView.as_view(), name="task_create"),
    # path("update/<int:pk>/", TaskUpdateView.as_view(), name="task_update"),
    # path("delete/<int:pk>/", delete_task_status.as_view(), name="task_delete"),
]
