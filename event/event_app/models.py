from django.db import models
from django.contrib.auth.models import User

class event_info(models.Model):
    Host_name = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    Event_details = models.CharField(max_length=500, default="")
    Location = models.CharField(max_length=500)
    Contact_details = models.CharField(max_length=500)

    def __str__(self):
        return f"Host : {self.Host_name}"