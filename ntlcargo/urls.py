from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("about-us",views.about,name="about-us"),
    path("contact",views.contact,name="contact-us"),
    path("login", views.login,name="login"),
]