from django.shortcuts import render
from projects.models import Projects


# Create your views here.
def all_projects(request):
    # query the db to return all project objects
    project = Projects.objects.all()
    return render(request, 'projects/all_projects.html', {'projects': project})
