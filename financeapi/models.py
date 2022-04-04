from django.db import models


class Hero(models.Model):
    name = models.CharField(max_length=200)
    alias = models.CharField(max_length=200)

    def __str__(self):
        return self.name
