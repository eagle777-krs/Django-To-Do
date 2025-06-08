from django.shortcuts import render, redirect
from django.urls import reverse


def main_view(request):
    if request.user.is_authenticated:
        return redirect(reverse('tasks:index'))
    return render(request, 'main.html')
