from django.db import models

class Task(models.Model):
    Firstname=models.TextField(max_length=50)
    Lastname=models.TextField(max_length=50)
    Email=models.EmailField()
    Age=models.IntegerField()

class User(models.Model):
    username=models.TextField(max_length=20)
    email=models.EmailField()
    password=models.TextField(max_length=50)