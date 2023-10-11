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
        return queryset.order_by("id")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        paginator = Paginator(self.object_list, self.paginate_by)
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
class StatusCreateView(CreateView):
    model = Status
    template_name = "projects/status_create.html"
    form_class = StatusForm
    success_message = "Creado con éxito."
    success_url = reverse_lazy("project:status_create")

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super(StatusCreateView, self).form_valid(form)


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
    status.delete()
    statuses = Status.objects.all()
    context = {"statuses": statuses}
    messages.success(request, "El estado se ha borrado exitosamente.")
    return render(request, "projects/status_list.html", context)


@method_decorator(login_required, name="dispatch")
class ProjectListView(ListView):
    model = Project
    template_name = "projects/project_list.html"
    context_object_name = "projects"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by("id")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        paginator = Paginator(self.object_list, self.paginate_by)
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

    # def get_queryset(self):
    #     """
    #     Asegura que solo se devuelvan los objetos que cumplan ciertas condiciones.
    #     """
    #     queryset = super().get_queryset()
    #     # Por ejemplo, filtramos solo los objetos que estén activos
    #     queryset = queryset.filter(estado="activo")
    #     return queryset


@method_decorator(login_required, name="dispatch")
class ProjectCreateView(CreateView):
    model = Project
    template_name = "projects/project_create.html"
    form_class = ProjectForm
    success_message = "Creado con éxito."
    success_url = reverse_lazy("project:project_create")

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super(ProjectCreateView, self).form_valid(form)


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
