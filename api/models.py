from asyncio.windows_events import NULL
import email
from tkinter import CASCADE
from tokenize import Special
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    name = models.CharField(max_length=40)
    contact = models.CharField(max_length=40)
    email = models.EmailField(max_length=60)
    defaultRate = models.DecimalField(max_digits=20, decimal_places=2)
    created_on = models.DateTimeField(auto_now_add=True)

class Timer(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()
    billed = models.BooleanField(default=False)
    note = models.TextField()
    specialRate = models.DecimalField(max_digits=20, decimal_places=2, null=True, default=NULL)