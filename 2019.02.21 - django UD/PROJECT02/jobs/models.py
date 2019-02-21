from django.db import models

# Create your models here.
class Job(models.Model):
    name = models.CharField(max_length=20)
    pastjob = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name   # admin에서 보여주기