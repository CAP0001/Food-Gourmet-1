from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView
from .forms import LoginForm, UpdateProfileForm
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.forms import UserCreationForm
from .models import Food, Feedback
from .models import UserProfile
from django.db.models import Avg


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

def HomeView(request):
    return render(request, "home.html")

@login_required
def Profile(request):
    message = "" 
    if request.method == "POST":
        form = UpdateProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            message = "Profile succesfuly saved!"
            form = UpdateProfileForm(instance=request.user)  
    else:
        form = UpdateProfileForm(instance=request.user)

    return render(request, "profile.html", {"form": form, "message": message})

def about_us(request):
    return render(request, "about_us.html")

def food(request):
    return render(request, "food.html")



def carbonara(request):
    item = get_object_or_404(Food, name="Pasta Carbonara")
    feedbacks = item.feedbacks.all().order_by('-created_at')

    if request.method == "POST" and request.user.is_authenticated:
        text = request.POST.get('feedback')
        stars = request.POST.get('stars') 
        
        if text and stars:
            Feedback.objects.create(
                food=item, 
                user=request.user, 
                text=text,
                stars=int(stars)
            )
            
            average = item.feedbacks.aggregate(Avg('stars'))['stars__avg']
            
            item.stars = average
            item.save()
            
            return redirect('carbonara')

    return render(request, "carbonara.html", {
        "item": item, 
        "feedbacks": feedbacks
    })

@login_required
def place_order(request):
    if request.method == "POST":
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)
        user_profile.orders_count += 1
        user_profile.save()
        
        return redirect('carbonara')
    
    return redirect('food')



# cap
#45354565434gdgfgrhfgef_!#$@#

#cap0001