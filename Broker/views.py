"""Properties Api view"""
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


#  create your views here.
from Broker.models.properties import Properties
from Broker.serializers.properties import PropertiesSerializer

# list all Properties
@api_view(['GET'])
def PropertiesList(request):
  data = Properties.objects.all()
  serializer = PropertiesSerializer(data, many=True)
  return Response(serializer.data)

# bring Properties by id
@api_view(['GET'])
def PropertiesDetail(request, pk):
  data = Properties.objects.get(id=pk)
  serializer = PropertiesSerializer(data, many=False)
  return Response(serializer.data)


