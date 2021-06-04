from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate, get_user_model


from .forms import UserRegistrationForm
# Create your views here.
def index(request):
    # if not request.user.is_authenticated:
    #     return HttpResponseRedirect(reverse('login'))
    return render(request, 'users/index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse('users:index'))
        else:
            return render(request, 'users/login.html', {
                'msg': "Invalid credentials"
            })

    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    return render(request, 'users/login.html', {
        'msg': "Logged out"
    })


def register_view(request):
    next = request.GET.get('next')
    form = UserRegistrationForm(request.POST or None)

    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)

        if next:
            return redirect(next)
        
        return redirect('/')

    context = {
        'form' : form
    }

    return render(request, 'users/signup.html', context)

def logout_view(request):
    logout(request)
    return redirect('/')