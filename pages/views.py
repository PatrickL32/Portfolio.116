from django.shortcuts import render

# Create your views here.
def homePageView(request):
    return render(request, 'pages/home.html')

def aboutPageView(request):
    return render(request, 'pages/about.html')

def projectsPageView(request):
    return render(request, 'pages/projects.html')