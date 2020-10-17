from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def dashboard(request):
    if request.user.is_superuser:
        users = User.objects.exclude(username=request.user)
        return render(request, 'dashboard.html', {'users':users})
    else:
        users = User.objects.filter(username=request.user)
        return render(request, 'dashboard.html', {'users':users})
