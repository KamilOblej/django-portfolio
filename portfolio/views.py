from django.shortcuts import render, redirect
# from django.views.generic import TemplateView
from . models import About, Skill, Project, ProjectImage, Icon
from django.http import JsonResponse

icons = Icon.objects.all()

i = {
    'icons': icons
}


def index(request):
    about = About.objects.all()
    skills = Skill.objects.all()
    projects = reversed(Project.objects.all()[Project.objects.count() - 3:])
    context = {
        'about': about,
        'skills': skills,
        'projects': projects,
    }

    context.update(i)

    print(context)

    return render(request, 'home.html', context)


def details(request, pk):
    project = Project.objects.filter(pk=pk)
    images = ProjectImage.objects.filter(project=pk)
    # project_json =
    context = {
        'project': project,
        'images': images,
    }

    context.update(i)

    print(context)
    return render(request, 'details.html', context)


def all_projects(request):
    projects = reversed(Project.objects.all())

    context = {
        'projects': projects
    }
    context.update(i)
    return render(request, 'projects.html', context)
