from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
)
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect


from .models import Status, Project
from .forms import StatusForm, ProjectForm


# Create your views here.


@method_decorator(login_required, name="dispatch")
class StatusListView(ListView):
    model = Status
    template_name = "projects/status_list.html"
    context_object_name = "statuses"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        # Filter by name
        search = self.request.GET.get("search", "")

        if search:
            queryset = queryset.filter(name__icontains=search)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get the total number of statuses
        context["total_statuses"] = self.model.objects.count()

        # pagination
        queryset = self.get_queryset()
        paginator = Paginator(queryset, self.paginate_by)
        page_number = self.request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        context["page_obj"] = page_obj
        context["is_paginated"] = page_obj.has_other_pages()
        previous_index = (
            page_obj.previous_page_number() - 1 if page_obj.has_previous() else 0
        )
        next_index = page_obj.next_page_number() - 1 if page_obj.has_next() else 0
        context["previous_index"] = previous_index
        context["next_index"] = next_index

        # Add search parameter to URL
        search = self.request.GET.get("search", "")
        if search:
            # Get the total number of statuses by filter
            context["total_search_statuses"] = self.model.objects.filter(
                name__icontains=search
            ).count()
            context["search"] = search

        return context


@method_decorator(login_required, name="dispatch")
class StatusCreateView(SuccessMessageMixin, CreateView):
    model = Status
    template_name = "projects/status_create.html"
    form_class = StatusForm
    success_message = "Creado con éxito."
    success_url = reverse_lazy("project:status_list")


@method_decorator(login_required, name="dispatch")
class StatusUpdateView(UpdateView):
    model = Status
    template_name = "projects/status_update.html"
    form_class = StatusForm
    success_message = "Actualizado con éxito."

    def get_success_url(self):
        return reverse_lazy("project:status_update", args=(self.object.pk,))

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super(StatusUpdateView, self).form_valid(form)


@login_required
def delete_project_status(request, project_status_id):
    status = Status.objects.get(id=project_status_id)
    status_name = status.name
    status.delete()
    messages.success(
        request, f"El estado '{status_name}' se ha borrado exitosamente.")
    return HttpResponseRedirect(reverse_lazy("project:status_list"))


@method_decorator(login_required, name="dispatch")
class ProjectListView(ListView):
    model = Project
    template_name = "projects/project_list.html"
    context_object_name = "projects"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        # Filter by name
        search = self.request.GET.get("search", "")
        # Filters
        status = self.request.GET.get("status", "")

        if search and status:
            queryset = queryset.filter(
                name__icontains=search, status__name=status)
        elif status:
            queryset = queryset.filter(status__name=status)
        elif search and status:
            queryset = queryset.filter(name__icontains=search)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get the total number of projects
        context["total_projects"] = self.model.objects.count()

        # Get the total number of projects by filter
        search = self.request.GET.get("search", "")
        context["total_search_projects"] = self.model.objects.filter(
            name__icontains=search
        ).count()

        # Get all statuses
        context["statuses"] = Status.objects.all()

        # pagination
        queryset = self.get_queryset()
        paginator = Paginator(queryset, self.paginate_by)
        page_number = self.request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        context["page_obj"] = page_obj
        context["is_paginated"] = page_obj.has_other_pages()
        previous_index = (
            page_obj.previous_page_number() - 1 if page_obj.has_previous() else 0
        )
        next_index = page_obj.next_page_number() - 1 if page_obj.has_next() else 0
        context["previous_index"] = previous_index
        context["next_index"] = next_index

        return context


@method_decorator(login_required, name="dispatch")
class ProjectDetailView(DetailView):
    model = Project
    template_name = "projects/project_detail.html"
    context_object_name = "project"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.get_object()
        profile = project.project_manager.profile
        if profile:
            context["profile_photo"] = profile.photo
        return context


@method_decorator(login_required, name="dispatch")
class ProjectCreateView(SuccessMessageMixin, CreateView):
    model = Project
    template_name = "projects/project_create.html"
    form_class = ProjectForm
    success_message = "Creado con éxito."
    success_url = reverse_lazy("project:project_list")


@method_decorator(login_required, name="dispatch")
class ProjectUpdateView(UpdateView):
    model = Project
    template_name = "projects/project_update.html"
    form_class = ProjectForm
    success_message = "Actualizado con éxito."

    def get_success_url(self):
        return reverse_lazy("project:project_update", args=(self.object.pk,))

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super(ProjectUpdateView, self).form_valid(form)


@login_required
def delete_project(request, project_id):
    project = Project.objects.get(id=project_id)
    project_name = project.name
    project.delete()
    messages.success(
        request, f"El proyecto '{project_name}' se ha borrado exitosamente."
    )
    return HttpResponseRedirect(reverse_lazy("project:project_list"))
