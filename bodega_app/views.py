from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "bodeapp/index.html")

def login(request):
    return render(request, "bodeapp/login.html")