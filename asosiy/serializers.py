from rest_framework.serializers import ModelSerializer
from .models import *

class AsosiySerializer(ModelSerializer):
    class Meta:
        model = Asosiy
        fields = '__all__'

class KaryuselSerializer(ModelSerializer):
    class Meta:
        model = KaryuselRasm
        fields = '__all__'

class KatalogSerializer(ModelSerializer):
    class Meta:
        model = Katalog
        fields = '__all__'

class FasadSerializer(ModelSerializer):
    class Meta:
        model = Fasad
        fields = '__all__'

class BizningUylarSerializer(ModelSerializer):
    class Meta:
        model = BizningUylar
        fields = '__all__'



