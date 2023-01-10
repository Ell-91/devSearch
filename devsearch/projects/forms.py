from django.forms import ModelForm
from .models import Project
from django import forms

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'featured_image' ,'description', 'demo_link', 'source_link', 'tags']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    # To make changes to title method /overrided the init method
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs) #inherits from ProjectForm

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input', 'placeholder': 'Add title'}) #go into the field and select the field we want to modify