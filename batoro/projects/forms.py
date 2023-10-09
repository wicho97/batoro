from django.forms import ModelForm

from .models import Status, Project


class StatusForm(ModelForm):
    class Meta:
        model = Status
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(StatusForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "c-input"
            visible.field.widget.attrs["autocomplete"] = "off"


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "c-input"
            visible.field.widget.attrs["autocomplete"] = "off"
