from django.urls import path
from restaurant_app import views

urlpatterns = [
    path('', views.HomeView, name='home'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/', views.Profile, name='profile'),
    path('about_us/', views.about_us, name='about_us'),
    path('foods/', views.FoodListView.as_view(), name='food-list'),
    path('basket/', views.basket, name='basket'),
    path('<int:pk>/', views.FoodDetailView.as_view(), name='food-detail'),
    path('checkout/', views.checkout, name='checkout'),\
    path('logout/', views.logout_view, name='logout'),
]