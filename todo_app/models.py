from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

alphanumeric=RegexValidator(r'^[0-9a-zA-z]*$','Only alphanumeric characters are allowed')

# Create your models here.
class Tasklist(models.Model):
    username=models.ForeignKey(User, on_delete=models.CASCADE)
    title= models.CharField(max_length=200,null=False)
    status=models.CharField(max_length=10,default="Incomplete")
    created_on=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    
class account(models.Model):
    username=models.CharField(max_length=20,null=False, validators=[alphanumeric])
    first_name=models.CharField(max_length=20,null=False)
    last_name=models.CharField(max_length=20,null=False)
    email=models.EmailField(max_length=100,null=False,validators=[alphanumeric])
    mobile=models.IntegerField(null=0)
    
    def __str__(self):
        return self.username