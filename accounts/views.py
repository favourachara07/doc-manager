from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, SigninForm

# Auths View
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # Extracting the form data
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']

            # Check password match
            if password1 != password2:
                messages.error(request, 'Passwords do not match')
            else:
                # Create user
                user = User.objects.create_user(
                    username=email,  # Use email as username
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=password1
                )
                user.save()
                print('user:', user)
                login(request, user)
                messages.success(request, 'Account created successfully!')
                return redirect('signin')# Redirect to a relevant page
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def signin_view(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)  # Use email as username
            if user is not None:
                login(request, user)
                return redirect(reverse('document_list'))   # Redirect after login
            else:
                print('Invalid email or password')
                messages.error(request, 'Invalid email or password')
    else:
        form = SigninForm()
    return render(request, 'signin.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('signin')  # Redirect to signin after logout
