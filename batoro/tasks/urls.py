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
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDetailView,
    delete_task,
    task_upload_attachment,
    task_download_attachment,
    task_delete_attachment,
    task_create_comment,
    export_csv
)


app_name = "task"

urlpatterns = [
    # Status
    path(route="status", view=StatusListView.as_view(), name="status_list"),
    path(route="status/create/", view=StatusCreateView.as_view(), name="status_create"),
    path(
        route="status/update/<int:pk>/",
        view=StatusUpdateView.as_view(),
        name="status_update",
    ),
    path(
        route="status/delete/<int:task_status_id>/",
        view=delete_task_status,
        name="status_delete",
    ),
    # Priority
    path(route="priority", view=PriorityListView.as_view(), name="priority_list"),
    path(
        route="priority/create/",
        view=PriorityCreateView.as_view(),
        name="priority_create",
    ),
    path(
        route="priority/update/<int:pk>/",
        view=PriorityUpdateView.as_view(),
        name="priority_update",
    ),
    path(
        route="priority/delete/<int:task_priority_id>/",
        view=delete_task_priority,
        name="priority_delete",
    ),
    # Type
    path(route="type", view=TypeListView.as_view(), name="type_list"),
    path(route="type/create/", view=TypeCreateView.as_view(), name="type_create"),
    path(
        route="type/update/<int:pk>/", view=TypeUpdateView.as_view(), name="type_update"
    ),
    path(
        route="type/delete/<int:task_type_id>/",
        view=delete_task_type,
        name="type_delete",
    ),
    # Tasks
    path(route="", view=TaskListView.as_view(), name="task_list"),
    path(route="create/", view=TaskCreateView.as_view(), name="task_create"),
    path(route="update/<int:pk>/", view=TaskUpdateView.as_view(), name="task_update"),
    path(route="detail/<int:pk>/", view=TaskDetailView.as_view(), name="task_detail"),
    path(route="delete/<int:task_id>/", view=delete_task, name="task_delete"),

    # Attachments
    path(route="attachment/<int:task_id>/", view=task_upload_attachment, name="task_upload_file"),
    path(route="attachment/download/<int:attachment_id>/", view=task_download_attachment, name="task_download_attachment"),
    path(route="attachment/delete/<int:attachment_id>/", view=task_delete_attachment, name="task_delete_attachment"),

    # Comments
    path(route="comment/<int:task_id>/", view=task_create_comment, name="task_create_comment"),

    # Reports
    path(route="export-csv/", view=export_csv, name="export_csv"),
]
