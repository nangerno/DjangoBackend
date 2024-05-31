from django.contrib import admin
from .models import TrainerModel, TrackModel, HorseModel, RaceResultModel, TrailResultModel, JockeyModel
# Register your models here.
admin.site.register([ TrainerModel, TrackModel, HorseModel, RaceResultModel, TrailResultModel, JockeyModel])