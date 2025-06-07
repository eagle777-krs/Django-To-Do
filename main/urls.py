from django.urls import path
from .views import main_view

app_name = 'main'

urlpatterns = [
    path('', main_view, name='main_page')]