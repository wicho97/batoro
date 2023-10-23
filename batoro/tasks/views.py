from django.views.generic import (
    ListView,
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

from .models import Status, Priority, Type, Task
from .forms import StatusForm, PriorityForm, TypeForm

# Create your views here.


@method_decorator(login_required, name="dispatch")
class StatusListView(ListView):
    model = Status
    template_name = "tasks/status_list.html"
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
    template_name = "tasks/status_create.html"
    form_class = StatusForm
    success_message = "Creado con éxito."
    success_url = reverse_lazy("task:status_list")


@method_decorator(login_required, name="dispatch")
class StatusUpdateView(UpdateView):
    model = Status
    template_name = "tasks/status_update.html"
    form_class = StatusForm
    success_message = "Actualizado con éxito."

    def get_success_url(self):
        return reverse_lazy("task:status_update", args=(self.object.pk,))

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super(StatusUpdateView, self).form_valid(form)


@login_required
def delete_task_status(request, task_status_id):
    status = Status.objects.get(id=task_status_id)
    status_name = status.name
    status.delete()
    messages.success(request, f"El estado '{status_name}' se ha borrado exitosamente.")
    return HttpResponseRedirect(reverse_lazy("task:status_list"))


@method_decorator(login_required, name="dispatch")
class PriorityListView(ListView):
    model = Priority
    template_name = "tasks/priority_list.html"
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
class PriorityCreateView(SuccessMessageMixin, CreateView):
    model = Priority
    template_name = "tasks/priority_create.html"
    form_class = PriorityForm
    success_message = "Creado con éxito."
    success_url = reverse_lazy("task:priority_list")


@method_decorator(login_required, name="dispatch")
class PriorityUpdateView(UpdateView):
    model = Priority
    template_name = "tasks/priority_update.html"
    form_class = PriorityForm
    success_message = "Actualizado con éxito."

    def get_success_url(self):
        return reverse_lazy("task:priority_update", args=(self.object.pk,))

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super(PriorityUpdateView, self).form_valid(form)


@login_required
def delete_task_priority(request, task_priority_id):
    status = Priority.objects.get(id=task_priority_id)
    status_name = status.name
    status.delete()
    messages.success(request, f"El estado '{status_name}' se ha borrado exitosamente.")
    return HttpResponseRedirect(reverse_lazy("task:priority_list"))


@method_decorator(login_required, name="dispatch")
class TypeListView(ListView):
    model = Type
    template_name = "tasks/type_list.html"
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
class TypeCreateView(SuccessMessageMixin, CreateView):
    model = Type
    template_name = "tasks/type_create.html"
    form_class = TypeForm
    success_message = "Creado con éxito."
    success_url = reverse_lazy("task:type_list")


@method_decorator(login_required, name="dispatch")
class TypeUpdateView(UpdateView):
    model = Type
    template_name = "tasks/type_update.html"
    form_class = TypeForm
    success_message = "Actualizado con éxito."

    def get_success_url(self):
        return reverse_lazy("task:type_update", args=(self.object.pk,))

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super(TypeUpdateView, self).form_valid(form)


@login_required
def delete_task_type(request, task_type_id):
    status = Type.objects.get(id=task_type_id)
    status_name = status.name
    status.delete()
    messages.success(request, f"El estado '{status_name}' se ha borrado exitosamente.")
    return HttpResponseRedirect(reverse_lazy("task:type_list"))


class TaskListView(ListView):
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = "tasks"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get the total number of tasks
        context["total_tasks"] = self.model.objects.count()

        # Get the total number of tasks by filter
        search = self.request.GET.get("search", "")
        context["total_search_tasks"] = self.model.objects.filter(
            subject__icontains=search
        ).count()

        # Get all statuses
        context["statuses"] = Status.objects.all()

        # Get all priorities
        context["priorities"] = Priority.objects.all()

        # Get all types
        context["types"] = Type.objects.all()

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


class TaskCreateView(CreateView):
    model = Task
    template_name = "tasks/task_create.html"
    fields = "__all__"


# class TaskUpdateView(UpdateView):
#     model = Task
#     template_name = "tasks/task_form.html"
#     fields = "__all__"


# class TaskDeleteView(DeleteView):
#     model = Task
#     template_name = "tasks/task_confirm_delete.html"
#     success_url = reverse_lazy("task:task_list")
