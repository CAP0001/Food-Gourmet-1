from django.urls import path
from restourant_app import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('', views.HomeView, name='home'), 
    path('register/', views.RegisterView.as_view(), name='register')
]
