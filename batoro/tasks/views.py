import csv
import datetime
import xlwt
import tempfile


from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
)
from django.urls import reverse, reverse_lazy
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic.edit import FormMixin
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from django.db.models import Sum

from .models import Status, Priority, Type, Task, Attachment, Comentary, Project
from .forms import (
    StatusForm,
    PriorityForm,
    TypeForm,
    TaskForm,
    TaskStatusAssignedToForm,
    AttachmentForm,
    CommentForm,
)

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
            page_obj.previous_page_number() if page_obj.has_previous() else 0
        )
        next_index = page_obj.next_page_number() if page_obj.has_next() else 0
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

        # pagination
        queryset = self.get_queryset()
        paginator = Paginator(queryset, self.paginate_by)
        page_number = self.request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        context["page_obj"] = page_obj
        context["is_paginated"] = page_obj.has_other_pages()
        previous_index = (
            page_obj.previous_page_number() if page_obj.has_previous() else 0
        )
        next_index = page_obj.next_page_number() if page_obj.has_next() else 0
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

        # pagination
        queryset = self.get_queryset()
        paginator = Paginator(queryset, self.paginate_by)
        page_number = self.request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        context["page_obj"] = page_obj
        context["is_paginated"] = page_obj.has_other_pages()
        previous_index = (
            page_obj.previous_page_number() if page_obj.has_previous() else 0
        )
        next_index = page_obj.next_page_number() if page_obj.has_next() else 0
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
    messages.success(request, f"El estado '{status_name}' se ha borrado exitosamente.")
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
        project = self.request.GET.get("project", "")
        date_from = self.request.GET.get("date_from", "")
        date_until = self.request.GET.get("date_until", "")

        filters = {}

        if search:
            filters["subject__icontains"] = search

        if status:
            filters["status__name"] = status

        if priority:
            filters["priority__name"] = priority

        if type:
            filters["type__name"] = type

        if project:
            filters["project__name"] = project

        if date_from:
            date_from = datetime.datetime.strptime(date_from, "%m/%d/%Y").strftime("%Y-%m-%d")
            filters["created_at__gte"] = date_from

        if date_until:
            date_until = datetime.datetime.strptime(date_until, "%m/%d/%Y").strftime("%Y-%m-%d")
            date_until = datetime.datetime.strptime(date_until, "%Y-%m-%d") + datetime.timedelta(hours=23, minutes=59, seconds=59)
            filters["created_at__lte"] = date_until

        queryset = queryset.filter(**filters).order_by("-created_at")

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
            page_obj.previous_page_number() if page_obj.has_previous() else 0
        )
        next_index = page_obj.next_page_number() if page_obj.has_next() else 0
        context["previous_index"] = previous_index
        context["next_index"] = next_index

        # Get the total number of records
        record_count = queryset.count()
        context["record_count"] = record_count

        context["statuses"] = Status.objects.all()

        context["priorities"] = Priority.objects.all()

        context["types"] = Type.objects.all()

        context["projects"] = Project.objects.all()

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
class TaskDetailView(FormMixin, DetailView):
    model = Task
    template_name = "tasks/task_detail.html"
    context_object_name = "task"
    form_class = TaskStatusAssignedToForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        task = self.get_object()

        attachments = Attachment.objects.filter(task=task.id)
        context["attachments"] = attachments

        comments = Comentary.objects.filter(task=task.id).order_by("-created_at")
        context["comments"] = comments

        if task.assigned_to:
            profile = task.assigned_to.profile
            if profile:
                context["profile_photo"] = profile.photo

        return context

    def get_initial(self):
        initial = super().get_initial()
        initial["status"] = self.object.status
        initial["assigned_to"] = self.object.assigned_to
        initial["estimated_time"] = self.object.estimated_time
        return initial

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        task = self.object
        new_status = form.cleaned_data.get("status")
        status_instance = Status.objects.get(name=new_status)
        task.status = status_instance

        new_assigned_to = form.cleaned_data.get("assigned_to")
        user_instance = User.objects.get(username=new_assigned_to)
        task.assigned_to = user_instance

        new_estimated_time = form.cleaned_data.get("estimated_time")
        task.estimated_time = new_estimated_time

        task.save()

        messages.success(self.request, "Datos actualizados.")
        return HttpResponseRedirect(self.request.path_info)


@login_required
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task_subject = task.subject
    task.delete()
    messages.success(request, f"La tarea '{task_subject}' se ha borrado exitosamente.")
    return HttpResponseRedirect(reverse_lazy("task:task_list"))


@login_required
def task_upload_attachment(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == "POST":
        form = AttachmentForm(request.POST, request.FILES)

        if form.is_valid():
            task = form.cleaned_data.get("task")
            file = form.cleaned_data.get("file")

            new_file = Attachment(
                file=file,
                task=task,
                user=request.user,
                size=file.size,
                mime_type=file.content_type,
            )
            new_file.save()

            return HttpResponseRedirect(reverse("task:task_detail", args=(task.id,)))
        else:
            messages.error(request, f"No se pudo subir los archivos.")
            return HttpResponseRedirect(reverse("task:task_detail", args=(task.id,)))

    messages.success(request, f"Los archivos se subieron exitosamente.")
    return HttpResponseRedirect(reverse("task:task_detail", args=(task.id,)))


@login_required
def task_download_attachment(request, attachment_id):
    attachment = Attachment.objects.get(pk=attachment_id)
    filename = attachment.file.name.split("/")[4]
    response = HttpResponse()
    response.content = attachment.file.read()
    response["Content-Disposition"] = "attachment; filename={0}".format(filename)
    return response


@login_required
def task_delete_attachment(request, attachment_id):
    attachment = Attachment.objects.get(pk=attachment_id)
    attachment.file.delete()
    attachment.delete()
    return JsonResponse({"success": True})


@login_required
def task_create_comment(request, task_id):
    task = Task.objects.get(id=task_id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.task = task
            comment.user = request.user
            comment.save()
            return HttpResponseRedirect(reverse("task:task_detail", args=(task.id,)))

    return HttpResponseRedirect(reverse("task:task_detail", args=(task.id,)))


@login_required
def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Reporte' + str(datetime.datetime.now()) + '.csv'

    writer = csv.writer(response)
    writer.writerow(['Fecha de creacion', 'Tarea', 'Horas Trabajadas'])

    total_hours = 0

    # Filters
    search = request.GET.get("search", "")
    status = request.GET.get("status", "")
    priority = request.GET.get("priority", "")
    type = request.GET.get("type", "")
    project = request.GET.get("project", "")
    date_from = request.GET.get("date_from", "")
    date_until = request.GET.get("date_until", "")

    filters = {}

    if search:
        filters["subject__icontains"] = search

    if status:
        filters["status__name"] = status

    if priority:
        filters["priority__name"] = priority

    if type:
        filters["type__name"] = type

    if project:
            filters["project__name"] = project

    if date_from:
            date_from = datetime.datetime.strptime(date_from, "%m/%d/%Y").strftime("%Y-%m-%d")
            filters["created_at__gte"] = date_from

    if date_until:
        date_until = datetime.datetime.strptime(date_until, "%m/%d/%Y").strftime("%Y-%m-%d")
        date_until = datetime.datetime.strptime(date_until, "%Y-%m-%d") + datetime.timedelta(hours=23, minutes=59, seconds=59)

    tasks = Task.objects.filter(**filters)

    for task in tasks:
        writer.writerow([task.created_at, task.subject, task.estimated_time])
        total_hours += task.estimated_time

    writer.writerow(['', 'Total de Horas trabajadas:', total_hours])

    return response


@login_required
def export_excel(request):
    workbook = xlwt.Workbook()

    worksheet = workbook.add_sheet('Reporte')

    total_hours = 0

    # Filters
    search = request.GET.get("search", "")
    status = request.GET.get("status", "")
    priority = request.GET.get("priority", "")
    type = request.GET.get("type", "")
    project = request.GET.get("project", "")
    date_from = request.GET.get("date_from", "")
    date_until = request.GET.get("date_until", "")

    filters = {}

    if search:
        filters["subject__icontains"] = search

    if status:
        filters["status__name"] = status

    if priority:
        filters["priority__name"] = priority

    if type:
        filters["type__name"] = type

    if project:
            filters["project__name"] = project

    if date_from:
            date_from = datetime.datetime.strptime(date_from, "%m/%d/%Y").strftime("%Y-%m-%d")
            filters["created_at__gte"] = date_from

    if date_until:
        date_until = datetime.datetime.strptime(date_until, "%m/%d/%Y").strftime("%Y-%m-%d")
        date_until = datetime.datetime.strptime(date_until, "%Y-%m-%d") + datetime.timedelta(hours=23, minutes=59, seconds=59)

    datos = Task.objects.filter(**filters)

    encabezados = ['Fecha de creacion', 'Tarea', 'Horas Trabajadas']
    for col, encabezado in enumerate(encabezados):
        worksheet.write(0, col, encabezado)

    for row, dato in enumerate(datos, start=1):
        worksheet.write(row, 0, dato.created_at.strftime('%Y-%m-%d %H:%M:%S'))
        worksheet.write(row, 1, dato.subject)
        worksheet.write(row, 2, dato.estimated_time)
        total_hours += dato.estimated_time

    row += 1

    worksheet.write(row, 1, 'Total de Horas trabajadas:')
    worksheet.write(row, 2, total_hours)

    for col in range(len(encabezados)):
        worksheet.col(col).width = 256 * 20

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Reporte' + str(datetime.datetime.now()) + '.xls'

    workbook.save(response)

    return response


@login_required
def export_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=Reporte' + str(datetime.datetime.now()) + '.pdf'
    response['Content-Transfer-Encoding'] = 'binary'

    # Filters
    search = request.GET.get("search", "")
    status = request.GET.get("status", "")
    priority = request.GET.get("priority", "")
    type = request.GET.get("type", "")
    project = request.GET.get("project", "")
    date_from = request.GET.get("date_from", "")
    date_until = request.GET.get("date_until", "")

    filters = {}

    if search:
        filters["subject__icontains"] = search

    if status:
        filters["status__name"] = status

    if priority:
        filters["priority__name"] = priority

    if type:
        filters["type__name"] = type

    if project:
            filters["project__name"] = project

    if date_from:
            date_from = datetime.datetime.strptime(date_from, "%m/%d/%Y").strftime("%Y-%m-%d")
            filters["created_at__gte"] = date_from

    if date_until:
        date_until = datetime.datetime.strptime(date_until, "%m/%d/%Y").strftime("%Y-%m-%d")
        date_until = datetime.datetime.strptime(date_until, "%Y-%m-%d") + datetime.timedelta(hours=23, minutes=59, seconds=59)

    tasks = Task.objects.filter(**filters)

    sum = tasks.aggregate(Sum('estimated_time'))

    html_string = render_to_string('tasks/pdf_output.html', {'tasks':tasks, 'total':sum['estimated_time__sum'], 'date': str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))})
    html = HTML(string=html_string, base_url=request.build_absolute_uri())

    result = html.write_pdf()

    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())

    return response