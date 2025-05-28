from django.urls import path
from . import views

urlpatterns = [
    path('', views.submit_email, name='submit_email'),
    path('success/', views.success, name='success'),
]
