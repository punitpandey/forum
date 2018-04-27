from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.
class query(models.Model):
    name=models.CharField(max_length=50)
    subject=models.CharField(max_length=150)
    query=models.CharField(max_length=1000)
    image=models.ImageField(upload_to='uploads')
    status=models.CharField(max_length=10,default='Active')
    lastactivedate=models.DateField(default=datetime.now().strftime('%Y-%m-%d'))
    def __str__(self):
        return self.subject
    class Meta:
        db_table="support_query"

class response(models.Model):
    query=models.ForeignKey('query',on_delete='CASCADE',default=1)
    responseUser=models.CharField(max_length=50,default="NULL")
    responsedate=models.DateField(default=datetime.now().strftime('%Y-%m-%d'))
    response=models.CharField(max_length=500)
    def __str__(self):
        return self.response
    class Meta:
        db_table="support_response"
    
