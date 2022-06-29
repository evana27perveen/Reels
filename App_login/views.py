from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, HttpResponseRedirect, reverse
from App_login.forms import SignupForm

# Create your views here.


def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_login:login'))
    content = {'form': form}
    return render(request, 'App_login/signup_page.html', context=content)


def log_in(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('App_main:home'))
    return render(request, 'App_login/login.html', context={'form': form})


def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('cover'))
