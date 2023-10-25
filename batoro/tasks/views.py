from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
)
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Status, Priority, Type, Task
from .forms import StatusForm, PriorityForm, TypeForm, TaskForm

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

        # Get the total number of records
        record_count = queryset.count()
        context["record_count"] = record_count

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
    messages.success(
        request, f"El estado '{status_name}' se ha borrado exitosamente.")
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

        # Get the total number of records
        record_count = queryset.count()
        context["record_count"] = record_count

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
    messages.success(
        request, f"El estado '{status_name}' se ha borrado exitosamente.")
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

        # Get the total number of records
        record_count = queryset.count()
        context["record_count"] = record_count

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
    messages.success(
        request, f"El estado '{status_name}' se ha borrado exitosamente.")
    return HttpResponseRedirect(reverse_lazy("task:type_list"))


@method_decorator(login_required, name="dispatch")
class TaskListView(ListView):
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = "tasks"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        # Filter by name
        search = self.request.GET.get("search", "")
        # Filters
        status = self.request.GET.get("status", "")
        priority = self.request.GET.get("priority", "")
        type = self.request.GET.get("type", "")

        if search:
            queryset = queryset.filter(subject__icontains=search)
        elif status and priority and type:
            queryset = queryset.filter(
                status__name=status, priority__name=priority, type__name=type)
        elif status and priority:
            queryset = queryset.filter(
                status__name=status, priority__name=priority)
        elif status and type:
            queryset = queryset.filter(status__name=status, type__name=type)
        elif priority and type:
            queryset = queryset.filter(
                priority__name=priority, type__name=type)
        elif status:
            queryset = queryset.filter(status__name=status)
        elif priority:
            queryset = queryset.filter(priority__name=priority)
        elif type:
            queryset = queryset.filter(type__name=type)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

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

        # Get the total number of records
        record_count = queryset.count()
        context["record_count"] = record_count

        # Get all statuses
        context["statuses"] = Status.objects.all()

        # Get all priorities
        context["priorities"] = Priority.objects.all()

        # Get all types
        context["types"] = Type.objects.all()

        return context


@method_decorator(login_required, name="dispatch")
class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "tasks/task_create.html"
    form_class = TaskForm
    success_message = "Creado con éxito."
    success_url = reverse_lazy("task:task_list")

    def form_valid(self, form):
        form.instance.creator = self.request.user
        messages.success(self.request, self.success_message)
        return super(TaskCreateView, self).form_valid(form)


@method_decorator(login_required, name="dispatch")
class TaskUpdateView(UpdateView):
    model = Task
    template_name = "tasks/task_update.html"
    form_class = TaskForm
    success_message = "Actualizado con éxito."

    def get_success_url(self):
        return reverse_lazy("task:task_update", args=(self.object.pk,))

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super(TaskUpdateView, self).form_valid(form)


@method_decorator(login_required, name="dispatch")
class TaskDetailView(DetailView):
    model = Task
    template_name = "tasks/task_detail.html"
    context_object_name = "task"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     project = self.get_object()
    #     profile = project.project_manager.profile
    #     if profile:
    #         context["profile_photo"] = profile.photo
    #     return context


@login_required
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task_subject = task.subject
    task.delete()
    messages.success(
        request, f"La tarea '{task_subject}' se ha borrado exitosamente."
    )
    return HttpResponseRedirect(reverse_lazy("task:task_list"))
