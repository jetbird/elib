from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Book(models.Model):
    title = models.CharField(max_length=255)
    num_pages = models.IntegerField()
    price = models.FloatField()
    authors = models.ManyToManyField(Author)
    is_read = models.BooleanField()

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('title',)
