from django.shortcuts import redirect,render
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import LoginForm

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
        

from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')


from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

def HomeView(request):
    return render(request, "home.html")

def Profile(request):
    return render(request, "profile.html")

def about_us(request):
    return render(request, "about_us.html")

def food(request):
    return render(request, "food.html")