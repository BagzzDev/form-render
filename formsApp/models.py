from django.db import models

# Create your models here.
class Login(models.Model):
    email = models.EmailField(unique=True, max_length=255)
    password = models.CharField(max_length=100)


    def __str__(self):
        return self.email
