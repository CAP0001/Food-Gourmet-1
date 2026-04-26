from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView, ListView, DetailView
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Avg
from django.db import transaction

from .forms import LoginForm, UpdateProfileForm
from .models import Food, Feedback, Basket, UserProfile

class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home') 

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, 'Невірний логін або пароль')
            return self.form_invalid(form)

class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

def logout_view(request):
    logout(request)
    return redirect('home') 

def HomeView(request):
    return render(request, "home.html")

@login_required
def Profile(request):
    message = "" 
    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == "POST":
        form = UpdateProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            message = "Profile successfully saved!"
            form = UpdateProfileForm(instance=request.user)  
    else:
        form = UpdateProfileForm(instance=request.user)

    return render(request, "profile.html", {"form": form, "message": message})

def about_us(request):
    return render(request, "about_us.html")

class FoodListView(ListView):
    model = Food
    context_object_name = "foods"
    template_name = "food_list.html" 

    def get_queryset(self):
        queryset = super().get_queryset()
        food_type = self.request.GET.get('type')
        if food_type and food_type != 'all':
            queryset = queryset.filter(food_type__iexact=food_type)
        return queryset

class FoodDetailView(DetailView):
    model = Food
    context_object_name = "food"
    template_name = "restaurant_app/food_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['feedbacks'] = self.object.feedbacks.all().order_by('-created_at')
        if self.request.user.is_authenticated:
            profile, _ = UserProfile.objects.get_or_create(user=self.request.user)
            context['user_status'] = profile.get_status()
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')

        self.object = self.get_object()
        action = request.POST.get('action')

        if action == 'make_order':
            cart_item, created = Basket.objects.get_or_create(user=request.user, food=self.object)
            if not created:
                cart_item.quantity += 1
            cart_item.save()
            return redirect('basket')

        elif action == 'add_feedback':
            text = request.POST.get('feedback')
            stars = request.POST.get('stars')
            if text and stars:
                Feedback.objects.create(
                    food=self.object,
                    user=request.user,
                    text=text,
                    stars=int(stars)
                )
                avg_rating = self.object.feedbacks.aggregate(Avg('stars'))['stars__avg']
                self.object.stars = avg_rating
                self.object.save()
            return redirect('food-detail', pk=self.object.pk)

        return redirect('food-detail', pk=self.object.pk)

@login_required
def basket(request):
    user_items = Basket.objects.filter(user=request.user)
    total_sum = sum(item.total_price() for item in user_items)
    return render(request, "restaurant_app/basket.html", {"items": user_items, "total_sum": total_sum})

@login_required
def checkout(request):
    if request.method == "POST":
        with transaction.atomic():
            user_basket = Basket.objects.filter(user=request.user)
            if user_basket.exists():
                total_quantity = sum(item.quantity for item in user_basket)
                profile, _ = UserProfile.objects.get_or_create(user=request.user)
                profile.orders_count += total_quantity
                profile.save()
                user_basket.delete()
    return redirect('basket')

# cap
#45354565434gdgfgrhfgef_!#$@#
#===================================
#cap0001
#1