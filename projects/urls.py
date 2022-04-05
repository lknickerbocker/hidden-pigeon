from django.urls import path

from .views import expand_project_hx, my_projects_view

app_name = "projects"
urlpatterns = [
    path("", view=my_projects_view, name="list"),
    path("expanded_hx/<int:pk>", view=expand_project_hx, name="expanded_project"),
]
