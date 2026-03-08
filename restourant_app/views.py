from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView
from .forms import LoginForm, UpdateProfileForm
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.forms import UserCreationForm

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
            message = "Профиль успешно обновлён!"
            form = UpdateProfileForm(instance=request.user)  
    else:
        form = UpdateProfileForm(instance=request.user)

    return render(request, "profile.html", {"form": form, "message": message})

def about_us(request):
    return render(request, "about_us.html")

def food(request):
    return render(request, "food.html")