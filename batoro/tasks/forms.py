from django.forms import ModelForm

from .models import Status, Priority, Type, Task, Attachment, Comentary


class StatusForm(ModelForm):
    class Meta:
        model = Status
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(StatusForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "c-input"
            visible.field.widget.attrs["autocomplete"] = "off"


class PriorityForm(ModelForm):
    class Meta:
        model = Priority
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(PriorityForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "c-input"
            visible.field.widget.attrs["autocomplete"] = "off"


class TypeForm(ModelForm):
    class Meta:
        model = Type
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(TypeForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "c-input"
            visible.field.widget.attrs["autocomplete"] = "off"


class TaskForm(ModelForm):
    class Meta:
        model = Task
        exclude = ["creator", "estimated_time"]

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "c-input"
            visible.field.widget.attrs["autocomplete"] = "off"


class TaskStatusAssignedToForm(ModelForm):
    class Meta:
        model = Task
        fields = ["status", "assigned_to"]

    def __init__(self, *args, **kwargs):
        super(TaskStatusAssignedToForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "c-input"
            visible.field.widget.attrs["autocomplete"] = "off"


class AttachmentForm(ModelForm):
    class Meta:
        model = Attachment
        fields = ["file", "task"]

class CommentForm(ModelForm):
    class Meta:
        model = Comentary
        fields = ["content"]