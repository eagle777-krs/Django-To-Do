from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.views import View
from django.urls import reverse
from django.contrib.auth import authenticate, login as auth_login, logout


class RegisterView(View):

    def get(self, request):
        form = RegisterForm()
        context = {'form': form}
        return render(request, 'register.html', context)

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect(reverse('tasks:index'))
        else:
            context = {'form':form}
            return render(request, 'register.html', context)

class LoginView(View):

    def get(self, request):
        form = LoginForm()
        context = {'form':form}
        return render(request, 'login.html', context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username'] #очищенные данные приведённые к нужно типу данных
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)# проверка пользователя в БД
            if user is not None:
                auth_login(request, user)
                return redirect(reverse('tasks:index'))
            else:
                form.add_error(None, 'Неверный логин или пароль')#ошибка при неверной авторизации
                context = {'form':form}
                return render(request, 'login.html', context)

def user_logout(request):
    logout(request)
    return redirect(reverse('main:main_page'))


