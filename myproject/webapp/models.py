from django.db import models


# Create your models here.

class pagedata(models.Model):
    Data_entry = models.IntegerField()
    User_id = models.CharField(max_length=15)
    Follows_count = models.IntegerField()
    Followers_count= models.IntegerField()
    Media_count= models.IntegerField()


class gender(models.Model):
    Male = models.IntegerField()
    Female = models.IntegerField()




