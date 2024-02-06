from django.contrib import admin

# Register your models here.
from .models import Project, Tag, Review

admin.site.register(Project) #Telling django to get this model and show it in the admin pannel
admin.site.register(Tag)
admin.site.register(Review)