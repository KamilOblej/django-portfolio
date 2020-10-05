from django.shortcuts import render
from django.views.generic import TemplateView
from . models import About, Skill


class HomeTemplateView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['about'] = About.objects.all()
        context['skills'] = Skill.objects.all()
        # context['project'] = Project.objects.all()

        return context
