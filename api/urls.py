from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.GetTaskInfoView.as_view(), name='task_info_api')
]