from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    picture = models.ImageField(blank=False, null=False)

    def __str__(self):
        return self.name


class Location(models.Model):
    locationID = models.AutoField(primary_key=True)
    userID = models.ForeignKey(User, on_delete= models.CASCADE, related_name='user_location', blank=True)
    lat = models.DecimalField(decimal_places=7, max_digits=15)
    lng = models.DecimalField(decimal_places=7, max_digits=15)
