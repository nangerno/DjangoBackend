from django.shortcuts import render
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import TreeModel
import json

# Create your views here.
def first_page(request):
    return render(request, 'crud.html', {})

class TreeView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            trees = list(TreeModel.objects.filter(id=id).values())
            print(trees)
            if len(trees) > 0:
                tree = trees[0]
                datos = {'message': "Success", 'tree': tree}
            else:
                datos = {'message': "trees not found..."}
            return JsonResponse(datos)
        else:
            trees = list(TreeModel.objects.values())
            print(trees)
            if len(trees) > 0:
                datos = {'message': "Success", 'tree': trees}
            else:
                datos = {'message': "trees not found..."}
            return JsonResponse(datos)

    def post(self, request):
        # print(request.body)
        jd = json.loads(request.body)
        # print(jd)
        TreeModel.objects.create(currentID=jd['currentID'], currentName=jd['currentName'], parrentID=jd['parrentID'], background=jd['background'], note=['note'], fontSize=['fontSize'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        trees = list(TreeModel.objects.filter(id=id).values())
        if len(trees) > 0:
            tree = TreeModel.objects.get(id=id)
            tree.currentID = jd['currentID']
            tree.currentName = jd['currentName']
            tree.parrentID = jd['parrentID']
            tree.background = jd['background']
            tree.note = jd['note']
            tree.fontSize = jd['fontSize']
            tree.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Company not found..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        trees = list(TreeModel.objects.filter(id=id).values())
        if len(trees) > 0:
            TreeModel.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "trees not found..."}
        return JsonResponse(datos)
