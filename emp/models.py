from django.db import models

# Create your models here.

class employee(models.Model):
    emp_name = models.CharField(max_length=30)
    team_number = models.IntegerField()
    emp_rank = models.CharField(max_length=30)
    emp_responsibilities = models.CharField(max_length=50)
    monthly_salary = models.IntegerField()
    entry_date = models.DateField(null=True)



