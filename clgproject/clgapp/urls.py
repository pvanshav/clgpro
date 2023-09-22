from . import views
from django.urls import path


urlpatterns = [

    path('',views.home,name='home'),
    path('index.html',views.home,name='index'),
    path('form.html',views.form,name='form'),
    path('login.html',views.login,name='login'),
    path('register.html',views.register,name='register'),



]