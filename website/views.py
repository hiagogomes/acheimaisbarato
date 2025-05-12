from django.shortcuts import render

def index(request):
    return render(request, 'website/index.html')

def avalie(request):
    return render(request, 'website/avalie.html')
