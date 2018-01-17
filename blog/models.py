from django.db import models

# Create your models here.
class blog(models.Model):
    chatagory=models.CharField(max_length=50)
    title=models.CharField(max_length=100)
    post=models.TextField(max_length=1000)

    def __str__(self):
        return self.title