from django.shortcuts import render

# Create your views here.

def index(request):
    return render (request, 'PageApp/index.html')

def page3(request):
    return render (request, "PageApp/page3.html")

def page4(request):
    return render (request, "PageApp/page4.html")