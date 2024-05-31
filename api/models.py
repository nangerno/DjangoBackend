from django.db import models

# Create your models here.
class TrainerModel(models.Model):
    name = models.CharField(max_length=50)
    list_horses = models.TextField()

class TrackModel(models.Model):
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    # it contains json type datas including distance of racing, record time of distance  / horse name,  condition of track
    description = models.TextField() 

class HorseModel(models.Model):
    name = models.CharField(max_length=50)
    # trainer, jockey, Sire/Dam, Horse Spell(date from to), Date when trainer changed(past trainers)
    owner = models.TextField()

class RaceResultModel(models.Model):
    track_name = models.CharField(max_length=50)
    horse_name_position = models.CharField(max_length=50)
    odds = models.CharField(max_length=50)
    margin = models.CharField(max_length=50)
    race_name = models.CharField(max_length=50)
    video_comment = models.TextField()
    steward_comment = models.TextField()
    barrior_horse_number = models.CharField(max_length=50)
    last_600m_race_time = models.CharField(max_length=50)
    race_time = models.CharField(max_length=50)
    position_at_800m = models.CharField(max_length=50)
    conditions = models.TextField()
    class_of_race = models.CharField(max_length=50)
class TrailResultModel(models.Model):
    date_trail = models.CharField(max_length=50)
    track_name = models.CharField(max_length=50)
    distance = models.CharField(max_length=50)
    conditions = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    race_time = models.CharField(max_length=50)
    horse_name = models.CharField(max_length=50)
class JockeyModel(models.Model):
    name = models.CharField(max_length=50)

    

