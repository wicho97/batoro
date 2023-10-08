from django.urls import path

from .views import StatusListView, StatusCreateView, StatusUpdateView, delete_project_status

app_name = "project"

urlpatterns = [
    path('status/', StatusListView.as_view(), name='status_list'),
    path('status/create/', StatusCreateView.as_view(), name='status_create'),
    path('status/update/<int:pk>/',
         StatusUpdateView.as_view(), name='status_update'),
    path('status/delete/<int:project_status_id>/',
         delete_project_status, name='status_delete'),
]
