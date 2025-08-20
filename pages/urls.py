from django.urls import path
from .views import homePageView, aboutPageView, projectsPageView

urlpatterns = [
    path('', homePageView, name='home'),
    path('about/', aboutPageView, name='about'),
    path('projects/', projectsPageView, name="projects")
]