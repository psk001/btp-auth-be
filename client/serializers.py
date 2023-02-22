from rest_framework import serializers
from .models import Otp
from .models import Image

class OtpSerializer(serializers.ModelSerializer):
    class Meta:
        model= Otp
        fields= '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'title', 'image')
    