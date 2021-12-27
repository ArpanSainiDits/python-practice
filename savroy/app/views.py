from django.shortcuts import render

# Create your views here.

def about(request):
    return render(request, 'about.html')


def components(request):
    return render(request, 'components.html')


def contact(request):
    return render(request, 'contact.html')


def index(request):
    return render(request, 'index.html')


def project(request):
    return render(request, 'project.html')


def sample(request):
    return render(request, 'sample-page.html')


def services(request):
    return render(request, 'services.html')
