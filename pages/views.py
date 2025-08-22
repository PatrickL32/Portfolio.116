from django.shortcuts import render
from  .import models

# Create your views here.
def aboutPageView(request):
    return render(request, 'pages/about.html')

def projectsPageView(request):
    projects_list = models.Project.objects.all()
    context = {
        'projects_list': projects_list
    }
    return render(request, 'pages/projects_list.html', context)
