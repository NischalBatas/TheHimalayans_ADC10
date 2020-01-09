from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_name=models.TextField()
    employee_address=models.TextField()
    employee_birth=models.TextField()
    employee_join_date=models.TextField()
    employee_salary=models.FloatField()
    employee_post=models.TextField()