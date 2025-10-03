from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'LandingPage.html')

def signinSignUp(request):
    return render(request, 'FacultySignIn.html')