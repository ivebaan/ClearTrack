from django.urls import path
from . import views

urlpatterns = [
    path('signinSignup/', views.home)
]