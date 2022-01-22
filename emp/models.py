from django.db import models
from django.contrib.auth.models import User
import uuid


# Create your models here.

class employee(models.Model):
    emp_uuid = str(uuid.uuid4()) # 임의의 랜덤 문자열
    emp_name = models.CharField(max_length=30)
    team_number = models.IntegerField()
    emp_rank = models.CharField(max_length=30)
    emp_responsibilities = models.CharField(max_length=50)
    monthly_salary = models.IntegerField()
    entry_date = models.DateField(null=True)

    image = models.ImageField(upload_to='emp/images/'+emp_uuid+'/', blank=True) #년월일이 아니라 사원 번호로 구분자를 주려면? 딱히 필요없나??=> 임의의 문자열 발생시켜서 하는 것으로
    empp = models.ForeignKey(User, on_delete=models.CASCADE())

    def __str__(self):
        return f'[{self.pk}]{self.emp_name}'

    def get_absolute_url(self):
        return f'/emp/{self.pk}/'
