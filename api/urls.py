from django.urls import path
from .views import TrainerView, TrackView, HorseView, RaceResultView, TrailResultView, JockeyView

urlpatterns = [
    path('trainer/', TrainerView.as_view(), name='trainer_list'),
    path('trainer/<int:id>', TrainerView.as_view(), name='trainer_process'),
    path('track/', TrackView.as_view(), name='track_list'),
    path('track/<int:id>', TrackView.as_view(), name='track_process'),
    path('horse/', HorseView.as_view(), name='horse_list'),
    path('horse/<int:id>', HorseView.as_view(), name='horse_process'),
    path('race_result/', RaceResultView.as_view(), name='race_result_list'),
    path('race_result/<int:id>', RaceResultView.as_view(), name='race_result_process'),
    path('trail_result/', TrailResultView.as_view(), name='trail_result_list'),
    path('trail_result/<int:id>', TrailResultView.as_view(), name='trail_result_process'),
    path('jockey/', JockeyView.as_view(), name='jockey_list'),
    path('jockey/<int:id>', JockeyView.as_view(), name='jockey_process'),
]