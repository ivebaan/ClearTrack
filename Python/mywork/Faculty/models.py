from django.db import models
from django.core.validators import EmailValidator

class Faculty(models.Model):
    DEPARTMENT_CHOICES = [
        ('library', 'Library'),
        ('accounting', 'Accounting'),
        ('acadaffairs', 'Academic Affairs'),
        ('studaffairs', 'Student Affairs'),
        ('itDepartment', 'IT Department'),
        ('plant', 'Physical Plant'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(
        unique=True,
        validators=[EmailValidator(message="Enter a valid school email address.")]
    )
    password = models.CharField(max_length=255)
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.department})"