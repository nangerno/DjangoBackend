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
        name = request.POST.get('name')
        list_horses = request.POST.get('list_of_horses')
        TrainerModel.objects.create(name=name, list_horses=list_horses)
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        put = QueryDict(request.body)
        name = put.get("name")
        list_horses = put.get("list_horses")
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
                datos = {'message': "trainer not found..."}
            return JsonResponse(datos)

    def post(self, request):
        # print(request.body)
        jd = json.loads(request.body)
        # print(jd)
        TrackModel.objects.create(address=jd['address'], phone=jd['phone'], description=['description'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        tracks = list(TrackModel.objects.filter(id=id).values())
        if len(tracks) > 0:
            track = TrackModel.objects.get(id=id)
            track.address = jd['address']
            track.phone = jd['phone']
            track.description = jd['description']
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
            datos = {'message': "tracks not found..."}
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
        # print(request.body)
        jd = json.loads(request.body)
        # print(jd)
        HorseModel.objects.create(name=jd['name'], owner=jd['owner'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        horses = list(HorseModel.objects.filter(id=id).values())
        if len(horses) > 0:
            horse = HorseModel.objects.get(id=id)
            horse.name = jd['name']
            horse.owner = jd['owner']
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
        # print(request.body)
        jd = json.loads(request.body)
        # print(jd)
        RaceResultModel.objects.create(track_name=jd['track_name'], horse_name_position=jd['horse_name_position'], odds=jd['odds'], margin=jd['margin'], race_name=jd['race_name'], video_comment=jd['video_comment'], steward_comment=jd['steward_comment'], barrior_horse_number=jd['barrior_horse_number'], last_600m_race_time=jd['last_600m_race_time'], race_time=jd['race_time'], position_at_800m=jd['position_at_800m'], conditions=jd['conditions'], class_of_race=jd['class_of_race'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        race_results = list(RaceResultModel.objects.filter(id=id).values())
        if len(race_results) > 0:
            race_result = RaceResultModel.objects.get(id=id)
            race_result.track_name = jd['track_name']
            race_result.horse_name_position = jd['horse_name_position']
            race_result.odds = jd['odds']
            race_result.margin = jd['margin']
            race_result.race_name = jd['race_name']
            race_result.video_comment = jd['video_comment']
            race_result.steward_comment = jd['steward_comment']
            race_result.barrior_horse_number = jd['barrior_horse_number']
            race_result.last_600m_race_time = jd['last_600m_race_time']
            race_result.race_time = jd['race_time']
            race_result.position_at_800m = jd['position_at_800m']
            race_result.conditions = jd['conditions']
            race_result.class_of_race = jd['class_of_race']
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
        # print(request.body)
        jd = json.loads(request.body)
        # print(jd)
        TrailResultModel.objects.create(date_trail=jd['date_trail'], track_name=jd['track_name'], distance=jd['distance'], position=jd['position'], race_time=jd['race_time'], horse_name=jd['horse_name'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        trail_results = list(TrailResultModel.objects.filter(id=id).values())
        if len(trail_results) > 0:
            trail_result = TrailResultModel.objects.get(id=id)
            trail_result.date_trail = jd['date_trail']
            trail_result.track_name = jd['track_name']
            trail_result.distance = jd['distance']
            trail_result.conditions = jd['conditions']
            trail_result.position = jd['position']
            trail_result.race_time = jd['race_time']
            trail_result.horse_name = jd['horse_name']
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
        # print(request.body)
        jd = json.loads(request.body)
        # print(jd)
        JockeyModel.objects.create(name=jd['name'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        jockeys = list(JockeyModel.objects.filter(id=id).values())
        if len(jockeys) > 0:
            jockey = TrailResultModel.objects.get(id=id)
            jockey.name = jd['name']
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