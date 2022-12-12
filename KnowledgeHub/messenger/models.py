from django.db import models
from django.contrib.auth.models import User
from datetime import *

# Create your models here.

class msg(models.Model):
    sender = models.ForeignKey(User, related_name="sender",on_delete=models.CASCADE)
    reciever = models.ForeignKey(User,related_name="reciever",on_delete=models.CASCADE)
    message = models.CharField(max_length=1000,default="")
    date = models.DateTimeField(auto_now_add=True)
    ordering = ['-date']

    def __str__(self):
        return self.sender.username + ' | ' + self.reciever.username

    def msgTime(self):
        h=int(str(self.date)[11:13])
        if h>11:
            return str(str(self.date)[11:16]+" PM")
        else:
            return str(str(self.date)[11:16]+" AM")
    
    def msgDate(self):
        y,m,d=str(self.date)[0:11].split('-')
        now = str(datetime.now())
        Y,M,D=str(now)[0:11].split('-')
        months=["January","February","March","April","May","June","July","August","September","October","November","December"]
        if y==Y and m==M and d==D:
            return "Today"
        else:
            return d+" "+months[int(m)-1]+" "+y

