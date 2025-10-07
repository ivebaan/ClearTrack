from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password, check_password
from .models import Faculty
from django.contrib.auth import authenticate, login

# Create your views here.
def home(request):
    return render(request, 'LandingPage.html')

def homepage(request):
    return render(request, 'Hompage.html')

def faculty_signin(request):
    if request.method == "POST":
        email = request.POST.get("username")
        password = request.POST.get("password")

        # Empty field validation
        if not email or not password:
            messages.error(request, "Please fill in both email and password.")
            return render(request, "FacultySignIn.html")

        # Check if user exists
        try:
            faculty = Faculty.objects.get(email=email)
        except Faculty.DoesNotExist:
            messages.error(request, "Invalid email or password.")
            return render(request, "FacultySignIn.html")

        # Password check
        if not check_password(password, faculty.password):
            messages.error(request, "Invalid email or password.")
            return render(request, "FacultySignIn.html")

        # Session persistence (manually)
        request.session["faculty_id"] = faculty.id
        request.session["faculty_name"] = f"{faculty.first_name} {faculty.last_name}"
        request.session.set_expiry(0)  # session ends on browser close

        messages.success(request, f"Welcome, {faculty.first_name}!")
        return redirect("homepage")

    return render(request, "FacultySignIn.html")

def faculty_signup(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        department = request.POST.get("department")

        # Field validation
        if not all([first_name, last_name, email, password, confirm_password, department]):
            messages.error(request, "All fields are required.")
            return render(request, "FacultySignUp.html")

        # Email format validation
        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "Enter a valid email address.")
            return render(request, "FacultySignUp.html")

        # Password confirmation
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, "FacultySignUp.html")

        # Duplicate check
        if Faculty.objects.filter(email=email).exists():
            messages.error(request, "This email is already registered.")
            return render(request, "FacultySignUp.html")

        # Create account
        Faculty.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=make_password(password),
            department=department
        )

        messages.success(request, "Account created successfully! You can now sign in.")
        return redirect("faculty_signin")

    return render(request, "FacultySignUp.html")