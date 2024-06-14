from django.shortcuts import render

def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about-us.html")

def contact(request):
    return render(request, "contact-us.html")

def login(request):
    return render(request, "login.html")


