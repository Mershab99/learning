from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    picture = models.ImageField(blank=False, null=False)

    def __str__(self):
        return self.name