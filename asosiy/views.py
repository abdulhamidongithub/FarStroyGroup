from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *

class AsosiyAPIView(APIView):
    def get(self, request):
        serializer = AsosiySerializer(Asosiy.objects.last())
        return Response(serializer.data)

class KaryusellarAPIView(APIView):
    def get(self, request):
        serializer = KaryuselSerializer(KaryuselRasm.objects.all(), many=True)
        return Response(serializer.data)

class KataloglarAPIView(APIView):
    def get(self, request):
        serializer = KatalogSerializer(Katalog.objects.all(), many=True)
        return Response(serializer.data)

class FasadlarAPIView(APIView):
    def get(self, request):
        serializer = FasadSerializer(Fasad.objects.all(), many=True)
        return Response(serializer.data)

class BizningUylarAPIView(APIView):
    def get(self, request):
        serializer = BizningUylarSerializer(BizningUylar.objects.all(), many=True)
        return Response(serializer.data)

