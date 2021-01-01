from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PlantSerializer, Plant


class PlantView(APIView):
    def get(self, request, *args, **kwargs):
        plants = Plant.objects.all()
        serializer = PlantSerializer(plants, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        plant_data = request.data
        serializer = PlantSerializer(data=plant_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
