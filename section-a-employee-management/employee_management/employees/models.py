from django.db import models

# Create your models here.
class Employee(models.Model):
    ACTIVE='ACTIVE'
    INACTIVE='INACTIVE'
    STATUS_CHOICES=[
        (ACTIVE,'Active'),(INACTIVE,'Inactive'),
    ]
    name=models.CharField(max_length=500)
    email=models.EmailField(unique=True,max_length=100)
    department=models.CharField(max_length=20)
    salary=models.IntegerField()
    status=models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=ACTIVE
    )