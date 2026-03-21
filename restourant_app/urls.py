from django.urls import path
from restourant_app import views

urlpatterns = [
    path('', views.HomeView, name='home'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/', views.Profile, name='profile'),
    path('about-us/', views.about_us, name='about_us'),
    path('food/', views.food, name='food'),
    path('carbonara/', views.carbonara, name='carbonara'),
    path('order/', views.place_order, name='place_order'),
    
]