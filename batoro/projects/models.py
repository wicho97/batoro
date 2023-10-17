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
    color = models.CharField(max_length=7, default="#000000")

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Statuses"

    def __str__(self):
        return self.name


class Project(TimestampMixin, models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    public = models.BooleanField()
    start_date = models.DateField(blank=True, null=True)
    finish_date = models.DateField(blank=True, null=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    project_manager = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="project_manager"
    )
    client = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="project_client",
    )

    def __str__(self):
        return self.name
