from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()

class Artist(models.Model):
    name = models.CharField(max_length=45)
    notes = models.TextField()
    songs = models.ManyToManyField(Song, related_name="artists")