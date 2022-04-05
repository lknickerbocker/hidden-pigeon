from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Project, Scene


@login_required
def my_projects_view(request):
    projects = Project.objects.filter(creator=request.user)
    return render(request, "projects.html", {"projects": projects})


def expand_project_hx(request, pk):

    project = Project.objects.get(id=pk)
    scenes = Scene.objects.filter(project_id=pk)

    return render(
        request,
        "partials/expanded_project.html",
        {"project": project, "scenes": scenes},
    )
