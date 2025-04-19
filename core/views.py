from django.shortcuts import render
# Create your views here.
def home (request):
    return render(request, 'index.html')
def services (request):
    return render(request, 'services.html')
def register (request):
    return render(request, 'register.html')
def login (request):
    return render(request, 'login.html')
def service_tracker (request):
    return render(request, 'serviceTracker.html')