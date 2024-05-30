from django.db import models

# Create your models here.
class TreeModel(models.Model):
    id = models.BigIntegerField(primary_key=True, unique=True, max_length=50)
    currentID = models.IntegerField(max_length=10)
    parrentID = models.IntegerField(max_length=10)
    currentName = models.CharField(max_length=50)
    background = models.CharField(max_length=50)
    note = models.TextField()
    fontSize = models.CharField(max_length=10)

class TrainerModel(models.Model):
    name = models.CharField(max_length=50)
    list_horsed = models.TextField()

class TrackModel(models.Model):
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    # it contains json type datas including distance of racing, record time of distance  / horse name,  condition of track
    description = models.TextField() 

class HorseModel(models.Model):
    name = models.CharField(max_length=50)

class RaceResult(models.Model):
    track_name = models.CharField(max_length=50)
    horse_name_position = models.CharField(max_length=50)
    odds = models.CharField(max_length=50)

class TrailResult(models.Model):
    date_trail = models.CharField(max_length=50)
    track_name = models.CharField(max_length=50)
    distance = models.CharField(max_length=50)
    conditions = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    race_time = models.CharField(max_length=50)
    horse_name = models.CharField(max_length=50)
    

