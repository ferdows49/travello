from django.db import models


class Destination(models.Model):
    name = models.CharField(max_length=100)
    detail = models.TextField(max_length=1000)
    price = models.IntegerField()
    image = models.ImageField(upload_to='pics')
    offer = models.BooleanField(default=False)

    def __str__(self):
        return self.name

