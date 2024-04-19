from .models import Resume, Project
from django.shortcuts import render
from django.core.paginator import Paginator


def index(request):
    resume = Resume.objects.first()
    return render(request, 'index.html',{'resume': resume})

def projects(request):
    projects = Project.objects.all()
    paginator = Paginator(projects, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'projects.html', {'page_obj': page_obj})

def connect(request):
    resume = Resume.objects.first()
    return render(request, 'connect.html',{'resume': resume})