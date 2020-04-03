from django.shortcuts import render, redirect
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login as my_login,
    logout as llogout
)

from .forms import UserLoginForm, UserRegisterForm


def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        my_login(request, user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "mainApp/login.html", context)


def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password, first_name=user.first_name, last_name=user.last_name)
        my_login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "mainApp/signup.html", context)


def logout_view(request):
    llogout(request)
    return redirect('/')


def index(request):
    return render(request, 'mainApp/homePage.html')

def contact(request):
    return render(request, 'mainApp/basic.html', {'contact':['Если у Вас остались вопросы, то задавайте их мне по телефону', '(063)-777-56-87']})
def login(request):
    return render(request, 'mainApp/login.html')
def signup(request):
    return render(request, 'mainApp/signup.html')
def recycle(request):
    return render(request, 'mainApp/recycle.html')
def cataclism(request):
    return render(request, 'mainApp/cataclism.html')
def rules(request):
    return render(request, 'mainApp/rules.html')
def companies(request):
    return render(request, 'mainApp/companies.html')
def companies1(request):
    return render(request, 'mainApp/companies1.html')
def companies2(request):
    return render(request, 'mainApp/companies2.html')


# Create your views here.
