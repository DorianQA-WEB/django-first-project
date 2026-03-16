from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    password = models.CharField(max_length=50)


    class Meta:
        db_table = "user"
