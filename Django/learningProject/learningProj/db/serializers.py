from rest_framework import serializers
from .models import User, Location

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class UserCardSerializer(serializers.ModelSerializer):
    user_location = LocationSerializer(many=True)

    def create(self, validated_data):
        locations = validated_data.pop('user_location')
        user = User.objects.create(**validated_data)
        for location in locations:
            Location.objects.create(userID=user, **location)
        return user

    class Meta:
        model = User
        fields = ('user_location', 'name', 'password')
