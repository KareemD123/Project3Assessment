from django.db import models

# Create your models here.


class Widget(models.Model):
    description = models.CharField(max_length=100)
    time = models.IntegerField()
    person = models.CharField(max_length=50)

    def __str__(self):
        return '%s' % (self.description)
