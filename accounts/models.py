from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    dob_year = models.IntegerField(blank=True, null=True)
    dob_month = models.IntegerField(blank=True, null=True)
    dob_day = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)
    student_id = models.CharField(max_length=50, blank=True, null=True)
    street_address1 = models.TextField(blank=True, null=True)
    street_address2 = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state_prov = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.CharField(max_length=20, blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    course = models.CharField(max_length=100, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
    

class VisitorLog(models.Model):
    DEPARTMENT_CHOICES = [
        ('HR', 'HR'),
        ('IT', 'IT'),
        ('Admin', 'Admin'),
        ('Finance', 'Finance'),
    ]
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Denied', 'Denied'),
    ]

    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES)
    name = models.CharField(max_length=255)
    address = models.TextField()
    purpose = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    contact = models.CharField(max_length=15)
    to_whom = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.department}"
