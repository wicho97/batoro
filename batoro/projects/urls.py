from django.urls import path

from .views import (
    StatusListView,
    StatusCreateView,
    StatusUpdateView,
    delete_project_status,
    ProjectListView,
    ProjectCreateView,
    ProjectUpdateView,
    ProjectDetailView,
)

app_name = "project"

urlpatterns = [
    # Status
    path("status/", StatusListView.as_view(), name="status_list"),
    path("status/create/", StatusCreateView.as_view(), name="status_create"),
    path("status/update/<int:pk>/", StatusUpdateView.as_view(), name="status_update"),
    path(
        "status/delete/<int:project_status_id>/",
        delete_project_status,
        name="status_delete",
    ),
    # Projects
    path("", ProjectListView.as_view(), name="project_list"),
    path("create/", ProjectCreateView.as_view(), name="project_create"),
    path("update/<int:pk>/", ProjectUpdateView.as_view(), name="project_update"),
    path("detail/<int:pk>/", ProjectDetailView.as_view(), name="project_detail"),
]
