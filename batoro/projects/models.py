from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class TimestampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Status(TimestampMixin, models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Statuses"

    def __str__(self):
        return self.name


class Project(TimestampMixin, models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    public = models.BooleanField()
    start_date = models.DateField()
    finish_date = models.DateField()
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    project_manager = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="project_manager"
    )
    client = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="project_client"
    )

    def __str__(self):
        return self.name
