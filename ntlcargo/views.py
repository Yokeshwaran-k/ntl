from django.contrib import messages
from django.shortcuts import  render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from .forms import  CreateUserForm

def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about-us.html")

def contact(request):
    return render(request, "contact-us.html")

def login(request):
    return render(request, "login.html")

def register(request):
    if request.method == 'POST':
        name = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 == password2:
            user = User.objects.create_user(username = name, email = email, password = password1)
            user.save()
            messages.success(request, 'Your account has been created successfully!')
            return redirect("login")
        else:
            messages.warning(request, 'Password mismatching!!')
            return redirect("register")


    else:
         form = CreateUserForm()
         return render(request, "register.html", {'form' : form})

        
   

'''def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Registered successfully")
    else:
        form = RegisterForm()
    return render(request, 'login.html', {'form': form})'''
    