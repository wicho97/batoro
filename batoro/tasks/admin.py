from django.contrib import admin
from .models import Status, Priority, Type, Task, Comentary, Attachment

# Register your models here.

admin.site.register(Status)
admin.site.register(Priority)
admin.site.register(Type)
admin.site.register(Task)
admin.site.register(Comentary)
admin.site.register(Attachment)
