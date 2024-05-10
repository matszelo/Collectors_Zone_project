from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm, UpdateProfileForm, ProfilePicForm, ChangePasswordForm
from .models import Profile


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Collectors_Zone:home')
        else:
            messages.success(request, 'Błąd! Sprawdź poprawność wpisanych danych i spróbuj jeszcze raz.', extra_tags='login')
            return redirect('login_user')

    else:
        return render(request, 'Loging_and_Register/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, 'Zostałeś poprawnie wylogowany!')
    return redirect('Collectors_Zone:home')


def register_user(request):
    form = RegisterForm(request.POST)
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Twoje konto zostało poprawnie zarejestrowane! Zaloguj się aby zacząć z niego korzystać.', extra_tags='register')
            return redirect('login_user')
        else:
            messages.success(request,'Błąd! Sprawdź poprawność wpisanych danych i spróbuj jeszcze raz.')
            return render(request, 'Loging_and_Register/register.html', {'form': form})

    return render(request, 'Loging_and_Register/register.html', {'form': form})


def user_profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        return render(request, 'Profile/user_profile.html', {'profile': profile})
    else:
        return redirect('Collectors_Zone:home')


def delete_profile(request, pk):
    profile = User.objects.get(pk=pk)
    profile.delete()
    messages.success(request, 'Twoje konto zostało usunięte.')
    return redirect('Collectors_Zone:home')


def update_profile(request, pk):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        profile = Profile.objects.get(user__id=request.user.id)
        user_form = UpdateProfileForm(request.POST or None, request.FILES or None, instance=current_user)
        profile_form = ProfilePicForm(request.POST or None, request.FILES or None, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Zmiany zostały poprawnie zapisane')
            return redirect('user_profile', pk)
        return render(request, 'Profile/update_profile.html',
                      {'profile': profile, 'user_form': user_form, 'profile_form': profile_form})
    else:
        return redirect('Collectors_Zone:home')


def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == 'POST':
            form = ChangePasswordForm(current_user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'Twoje hasło zostało poprawnie zmienione. Zaloguj się ponownie używając nowego hasła', extra_tags='password_change')
                return redirect('login_user')
            else:
                messages.success(request,'Błąd! Sprawdź poprawność wpisanych danych i spróbuj jeszcze raz.')
                return render(request,'Profile/password_change.html', {'form': form})
        else:
            form = ChangePasswordForm(current_user)
            return render(request, 'Profile/password_change.html', {'form': form})
    else:
        return redirect('Collectors_Zone:home')
