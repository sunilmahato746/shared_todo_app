from django.db import models

# Create your models here.
class TodoItem(models.Model):
    content=models.TextField()
    Urgent = models.BooleanField(null=True)
    Important = models.BooleanField(null=True)
    Datelogged= models.DateTimeField(null=True)
    Targetdate = models.DateTimeField(null=True)
    Flag=models.BooleanField(null=False)
