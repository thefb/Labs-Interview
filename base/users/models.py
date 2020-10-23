from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100, unique=True, primary_key=True)
    friends = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return f"{self.name}"
