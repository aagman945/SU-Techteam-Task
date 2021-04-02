from django.db import models

# Create your models here.
class Contactus(models.Model):
    Username = models.CharField(max_length=122, null=True)
    Email = models.CharField(max_length=122, null=True)
    Desc = models.TextField(null=True)
    date = models.DateTimeField()

    def __str__(self):
        return self.Username