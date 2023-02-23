from rest_framework import serializers
from .models import Otp, Image, Election, ElectionCandidate


class OtpSerializer(serializers.ModelSerializer):
    class Meta:
        model= Otp
        fields= '__all__'

class ElectionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Election
        fields= '__all__'


class ElectionCandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model= ElectionCandidate
        fields= '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'title', 'image')
    