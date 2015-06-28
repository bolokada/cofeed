from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

#creation d'une classe qui va herite des pptes de la vue du projet TemplateView
class SplashView(TemplateView):
	template_name = "index.html"