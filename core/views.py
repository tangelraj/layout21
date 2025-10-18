from django.shortcuts import render

def index(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')

def schools(request):
    return render(request, 'core/schools.html')

def pricing(request):
    return render(request, 'core/price.html')

def library(request):
    return render(request, 'core/lib.html')

def story(request):
    return render(request, 'core/story.html')
