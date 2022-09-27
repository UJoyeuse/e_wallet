from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.transfer, name="dashboard"),
    path('about', views.about_view, name="about"),
    path('contact', views.contact_view, name='contact'),
    path('accounts', views.account_view, name='accounts'),



]
