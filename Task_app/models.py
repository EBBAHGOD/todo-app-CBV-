from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task_list(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    task_name=models.CharField(max_length=100,null=False,blank=False)
    task_description=models.TextField(blank=True,null=True)
    completed=models.BooleanField(default=False)
    task_date=models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.task_name

