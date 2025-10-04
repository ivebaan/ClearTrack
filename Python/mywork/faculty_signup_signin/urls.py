from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD:Python/mywork/faculty_signup_signin/urls.py
    path('signin-signup/', views.home)
=======
    path('GradeFlow/', views.home, name='GradeFlow'),
    path('FacultySignInSignUp/', views.signinSignUp, name='FacultySignInSignUp')
>>>>>>> 3e9da778c4237906f2016c0087372cd696389b43:Python/mywork/faculty_Signin_Signup/urls.py
]