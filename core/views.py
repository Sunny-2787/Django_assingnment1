from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def no(request):
    return render(request,'no.html')