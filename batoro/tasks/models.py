from django.db import models
from django.contrib.auth.models import User


from projects.models import Project


# Create your models here.


class TimestampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CustomModel(TimestampMixin, models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=7, default="#000000")

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Status(CustomModel):
    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Statuses"


class Priority(CustomModel):
    class Meta:
        verbose_name = "Priority"
        verbose_name_plural = "Priorities"


class Type(CustomModel):
    class Meta:
        verbose_name = "Type"
        verbose_name_plural = "Types"


class Task(TimestampMixin, models.Model):
    subject = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    priority = models.ForeignKey(Priority, on_delete=models.SET_NULL, null=True)
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)
    creator = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name="task_creator", null=True
    )
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="task_assigned_to",
    )
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    start_date = models.DateField(blank=True, null=True)
    finish_date = models.DateField(blank=True, null=True)
    estimated_time = models.FloatField(default=0)

    def __str__(self):
        return self.id, self.subject


class Comentary(TimestampMixin, models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name="comentary_user", null=True
    )
    task = models.ForeignKey(
        Task, on_delete=models.SET_NULL, related_name="comentary_task", null=True
    )
    content = models.TextField()

    def __str__(self):
        return self.user + ": " + self.task


class Attachment(TimestampMixin, models.Model):
    file = models.FileField(upload_to="file/%Y/%m/%d/", max_length=100, blank=True)
    task = models.ForeignKey(
        Task, related_name="attachments_task", on_delete=models.CASCADE, null=True
    )
    user = models.ForeignKey(
        User, related_name="attachments_user", on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return self.file.name.split('/')[4] #returns file handle name

