from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"
    
class NewsPageView(TemplateView):
    template_name = "new.html"    
    
class ServicesPageView(TemplateView):
    template_name = "services.html"        