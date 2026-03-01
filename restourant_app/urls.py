from django.urls import path
from restourant_app import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('home/', views.HomeView, name='home'),  # додайте домашню сторінку
    path('register/', views.RegisterView.as_view(), name='register')
]
