from django.urls import path
from . import views

urlpatterns = [
    path('GradeFlow/', views.home, name='GradeFlow'),
    path('FacultySignInSignUp/', views.signinSignUp, name='FacultySignInSignUp')
]