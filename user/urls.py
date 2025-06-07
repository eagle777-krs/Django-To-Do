from django.urls import path
from .views import RegisterView, LoginView, user_logout

app_name = 'user'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', user_logout, name='logout')]