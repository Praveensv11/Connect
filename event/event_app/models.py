from django.db import models
from django.contrib.auth.models import User

class event_info(models.Model):
    Host_name = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    Event_details = models.CharField(max_length=500, default="")
    Location = models.CharField(max_length=500)
    Contact_details = models.CharField(max_length=500)

    def __str__(self):
        return f"Host : {self.Host_name}"
    
class Chat(models.Model):
    name = models.CharField(max_length=64, default="")
    chat = models.CharField(max_length=10000, default="")

    def __str__(self):
        return f"{self.name} ({self.chat})"
    
class ReportUser(models.Model):
    victim = models.CharField(max_length=64, default="")
    reported_user = models.CharField(max_length=64, default="")
    report = models.CharField(max_length=1000, default="")

    def __str__(self):
        return f"{self.victim} : {self.reported_user}"