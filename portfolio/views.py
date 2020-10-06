from django.shortcuts import render, redirect
# from django.views.generic import TemplateView
from . models import About, Skill, Project, ProjectImage
from django.http import JsonResponse


# class HomeTemplateView(TemplateView):
#     template_name = "home.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#         context['about'] = About.objects.all()
#         context['skills'] = Skill.objects.all()
#         context['projects'] = Project.objects.all()

#         return context

# def details(self, request):
#     return render('./details.html')

def index(request):
    about = About.objects.all()
    skills = Skill.objects.all()
    projects = Project.objects.all()

    context = {
        'about': about,
        'skills': skills,
        'projects': projects,
    }

    print(context)

    return render(request, 'home.html', context)


def details(request, pk):
    project = Project.objects.filter(pk=pk)
    # project_json =
    context = {
        'project': project,
    }

    print(context)
    return render(request, 'details.html', context)
