from django.shortcuts import render
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.http import QueryDict
from .models import TrainerModel, TrackModel, HorseModel, RaceResultModel, TrailResultModel, JockeyModel
import json

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class TrainerView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            trainers = list(TrainerModel.objects.filter(id=id).values())
            if len(trainers) > 0:
                trainer = trainers[0]
                datos = {'message': "Success", 'trainer': trainer}
            else:
                datos = {'message': "trainer not found..."}
            return JsonResponse(datos)
        else:
            trainers = list(TrainerModel.objects.values())
            if len(trainers) > 0:
                datos = {'message': "Success", 'trainers': trainers}
            else:
                datos = {'message': "trainer not found..."}
            return JsonResponse(datos)

    def post(self, request):
        TrainerModel.objects.create(name=request.POST.get('name'), list_horses=request.POST.get('list_horses'))
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        name = QueryDict(request.body).get("name")
        list_horses = QueryDict(request.body).get("list_horses")
        print(list_horses)
        trainers = list(TrainerModel.objects.filter(id=id).values())
        if len(trainers) > 0:
            trainer = TrainerModel.objects.get(id=id)
            trainer.name = name
            trainer.list_horses = list_horses
            trainer.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "trainer not found..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        trainers = list(TrainerModel.objects.filter(id=id).values())
        if len(trainers) > 0:
            TrainerModel.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "trainers not found..."}
        return JsonResponse(datos)

class TrackView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            tracks = list(TrackModel.objects.filter(id=id).values())
            if len(tracks) > 0:
                track = tracks[0]
                datos = {'message': "Success", 'track': track}
            else:
                datos = {'message': "track not found..."}
            return JsonResponse(datos)
        else:
            tracks = list(TrackModel.objects.values())
            if len(tracks) > 0:
                datos = {'message': "Success", 'tracks': tracks}
            else:
                datos = {'message': "tracks not found..."}
            return JsonResponse(datos)

    def post(self, request):
        TrackModel.objects.create(address=request.POST.get('address'), phone=request.POST.get('phone'), description=request.POST.get('description'))
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        tracks = list(TrackModel.objects.filter(id=id).values())
        if len(tracks) > 0:
            track = TrackModel.objects.get(id=id)
            track.address = QueryDict(request.body).get("address")
            track.phone = QueryDict(request.body).get("phone")
            track.description = QueryDict(request.body).get("description")
            track.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "track not found..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        tracks = list(TrackModel.objects.filter(id=id).values())
        if len(tracks) > 0:
            TrackModel.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "track not found..."}
        return JsonResponse(datos)

class HorseView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            horses = list(HorseModel.objects.filter(id=id).values())
            if len(horses) > 0:
                horse = horses[0]
                datos = {'message': "Success", 'horse': horse}
            else:
                datos = {'message': "horse not found..."}
            return JsonResponse(datos)
        else:
            horses = list(HorseModel.objects.values())
            if len(horses) > 0:
                datos = {'message': "Success", 'horses': horses}
            else:
                datos = {'message': "horses not found..."}
            return JsonResponse(datos)

    def post(self, request):
        HorseModel.objects.create(name=request.POST.get('name'), owner=request.POST.get('owner'))
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        horses = list(HorseModel.objects.filter(id=id).values())
        if len(horses) > 0:
            horse = HorseModel.objects.get(id=id)
            horse.name = QueryDict(request.body).get("name")
            horse.owner = QueryDict(request.body).get("owner")
            horse.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "horse not found..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        horses = list(HorseModel.objects.filter(id=id).values())
        if len(horses) > 0:
            HorseModel.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "horses not found..."}
        return JsonResponse(datos)
    
class RaceResultView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            race_results = list(RaceResultModel.objects.filter(id=id).values())
            if len(race_results) > 0:
                race_result = race_results[0]
                datos = {'message': "Success", 'race_result': race_result}
            else:
                datos = {'message': "race_result not found..."}
            return JsonResponse(datos)
        else:
            rece_results = list(RaceResultModel.objects.values())
            if len(rece_results) > 0:
                datos = {'message': "Success", 'rece_results': rece_results}
            else:
                datos = {'message': "rece_results not found..."}
            return JsonResponse(datos)

    def post(self, request):
        RaceResultModel.objects.create(track_name=request.POST.get('track_name'), horse_name_position=request.POST.get('horse_name_position'), odds=request.POST.get('odds'), margin=request.POST.get('margin'), race_name=request.POST.get('race_name'), video_comment=request.POST.get('video_comment'), steward_comment=request.POST.get('steward_comment'), barrior_horse_number=request.POST.get('barrior_horse_number'), last_600m_race_time=request.POST.get('last_600m_race_time'), race_time=request.POST.get('race_time'), position_at_800m=request.POST.get('position_at_800m'), conditions=request.POST.get('conditions'), class_of_race=request.POST.get('class_of_race'))
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        race_results = list(RaceResultModel.objects.filter(id=id).values())
        if len(race_results) > 0:
            race_result = RaceResultModel.objects.get(id=id)
            race_result.track_name = QueryDict(request.body).get("track_name")
            race_result.horse_name_position = QueryDict(request.body).get("horse_name_position")
            race_result.odds = QueryDict(request.body).get("odds")
            race_result.margin = QueryDict(request.body).get("margin")
            race_result.race_name = QueryDict(request.body).get("race_name")
            race_result.video_comment = QueryDict(request.body).get("video_comment")
            race_result.steward_comment = QueryDict(request.body).get("steward_comment")
            race_result.barrior_horse_number = QueryDict(request.body).get("barrior_horse_number")
            race_result.last_600m_race_time = QueryDict(request.body).get("last_600m_race_time")
            race_result.race_time = QueryDict(request.body).get("race_time")
            race_result.position_at_800m = QueryDict(request.body).get("position_at_800m")
            race_result.conditions = QueryDict(request.body).get("conditions")
            race_result.class_of_race = QueryDict(request.body).get("class_of_race")
            race_result.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "race_result not found..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        race_results = list(RaceResultModel.objects.filter(id=id).values())
        if len(race_results) > 0:
            RaceResultModel.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "race_result not found..."}
        return JsonResponse(datos)

class TrailResultView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            trail_results = list(TrailResultModel.objects.filter(id=id).values())
            if len(trail_results) > 0:
                trail_result = trail_results[0]
                datos = {'message': "Success", 'trail_result': trail_result}
            else:
                datos = {'message': "race_result not found..."}
            return JsonResponse(datos)
        else:
            trail_results = list(TrailResultModel.objects.values())
            if len(trail_results) > 0:
                datos = {'message': "Success", 'trail_results': trail_results}
            else:
                datos = {'message': "trail_results not found..."}
            return JsonResponse(datos)

    def post(self, request):
        TrailResultModel.objects.create(date_trail=request.POST.get('date_trail'), track_name=request.POST.get('track_name'), distance=request.POST.get('distance'), position=request.POST.get('position'), race_time=request.POST.get('race_time'), horse_name=request.POST.get('horse_name'))
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        trail_results = list(TrailResultModel.objects.filter(id=id).values())
        if len(trail_results) > 0:
            trail_result = TrailResultModel.objects.get(id=id)
            trail_result.date_trail = QueryDict(request.body).get("date_trail")
            trail_result.track_name = QueryDict(request.body).get("track_name")
            trail_result.distance = QueryDict(request.body).get("distance")
            trail_result.conditions = QueryDict(request.body).get("conditions")
            trail_result.position = QueryDict(request.body).get("position")
            trail_result.race_time = QueryDict(request.body).get("race_time")
            trail_result.horse_name = QueryDict(request.body).get("horse_name")
            trail_result.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "trail_result not found..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        trail_result = list(TrailResultModel.objects.filter(id=id).values())
        if len(trail_result) > 0:
            TrailResultModel.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "trail_result not found..."}
        return JsonResponse(datos)

class JockeyView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            jockeys = list(JockeyModel.objects.filter(id=id).values())
            if len(jockeys) > 0:
                jockey = jockeys[0]
                datos = {'message': "Success", 'jockey': jockey}
            else:
                datos = {'message': "jockey not found..."}
            return JsonResponse(datos)
        else:
            jockeys = list(JockeyModel.objects.values())
            if len(jockeys) > 0:
                datos = {'message': "Success", 'jockeys': jockeys}
            else:
                datos = {'message': "jockeys not found..."}
            return JsonResponse(datos)

    def post(self, request):
        JockeyModel.objects.create(name=request.POST.get('name'))
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jockeys = list(JockeyModel.objects.filter(id=id).values())
        if len(jockeys) > 0:
            jockey = TrailResultModel.objects.get(id=id)
            jockey.name = QueryDict(request.body).get("name")
            jockey.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "jockey not found..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        jockey = list(JockeyModel.objects.filter(id=id).values())
        if len(jockey) > 0:
            JockeyModel.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "jockey not found..."}
        return JsonResponse(datos)