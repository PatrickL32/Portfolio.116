from django.urls import path
from pages import views

urlpatterns = [
    path('', views.about_me, name='about_me'),
    path('experience/',views.experience, name='experience'),
    path('contact/',views.contact_view, name='contact' ),
    path('projects/',views.projects_list, name="projects"),
]
