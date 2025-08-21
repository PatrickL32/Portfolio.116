from django.urls import path
from .views import  aboutPageView, projectsPageView

urlpatterns = [
    path('about/', aboutPageView, name='about'),
    path('projects/', projectsPageView, name="projects"),
]