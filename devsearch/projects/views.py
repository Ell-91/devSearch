from django.shortcuts import render, redirect
from .models import Project
from django.http import HttpResponse
from . forms import ProjectForm



def projects(request):
    projects = Project.objects.all()
    context =  {'projects': projects}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    project = Project.objects.get(id = pk)
    tags = project.tags.all()
    print('project', project)
    return render(request, 'projects/single-project.html', {'project': project, 'tags': tags})

def createProject(request):
    form = ProjectForm()

    #once a form is sucessfully submitted we want to redirect and send them to the
    #projects page
    if request.method == 'POST':
        print(request.POST)
        form = ProjectForm(request.POST, request.FILES) #instantiate form class and pass in data
        if form.is_valid(): #checks if all required fields are valid 
            form.save()
            return redirect('projects') # form successfully submitted, redirect people to the projects page
             
    context = {'form' : form}
    return render(request, 'projects/project_form.html', context)

def updateProject(request, pk):
    project = Project.objects.get(id = pk)
    form = ProjectForm(instance = project)

    #once a form is sucessfully submitted we want to redirect and send them to the
    #projects page
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance = project)
        if form.is_valid():
            form.save()
            return redirect('projects')
             
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)

def deleteProject(request, pk):
    project = Project.objects.get(id=pk) #get object by id/primary key   // here we query the object or the project
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project} #pass that into the context dictionary as an object
    return render(request, 'projects/delete_template.html', context )