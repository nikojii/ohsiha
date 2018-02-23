from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from ohsiha.core.forms import RegisterForm

def register(request):
	if request.user.is_authenticated:
		return redirect('home')
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('home')
	else:
		form = RegisterForm()
	return render(request, 'register.html', {'form': form})

def signin(request):
	if request.user.is_authenticated:
		return redirect('home')
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('home')
		else:
			print(form.errors)
			print(form.non_field_errors)
	else:
		form = AuthenticationForm()

	return render(request, 'login.html', {'form': form})

def home(request):
	return render(request, 'home.html',)

def signout(request):
	logout(request)
	return redirect('home')