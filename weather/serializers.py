from rest_framework import serializers
from datetime import datetime
from django.core.exceptions import ValidationError

from weather.models import WeatherEntity

class WeatherEntitySerializer(serializers.Serializer):
    temperature = serializers.FloatField()
    city = serializers.CharField(max_length=100, required=False)
    atmosphericPressure = serializers.CharField(max_length=100, required=False)
    humidity = serializers.CharField(max_length=100, required=False)
    weather = serializers.CharField(max_length=100, required=False)
    date = serializers.DateTimeField()

    def validate_temperature(self, value):
        if not isinstance(value, (int, float)):
            raise serializers.ValidationError("Temperature must be a number.")
        return value

    def validate_date(self, value):
        if not isinstance(value, datetime):
            raise serializers.ValidationError("Date must be a datetime object.")
        return value

    def create(self, validated_data):
        return WeatherEntity(**validated_data)

    def update(self, instance, validated_data):
        instance.temperature = validated_data.get('temperature', instance.temperature)
        instance.city = validated_data.get('city', instance.city)
        instance.atmosphericPressure = validated_data.get('atmosphericPressure', instance.atmosphericPressure)
        instance.humidity = validated_data.get('humidity', instance.humidity)
        instance.weather = validated_data.get('weather', instance.weather)
        instance.date = validated_data.get('date', instance.date)
        return instance
