from rest_framework import serializers
from .models import Weather

class DataSerializer(serializers.ModelSerializer):
	DATE = serializers.CharField(max_length=8, min_length=7, allow_blank=False, trim_whitespace=True)
	TMAX = serializers.FloatField()
	TMIN = serializers.FloatField()
	class Meta:
		model = Weather
		fields = ['DATE', 'TMAX', 'TMIN']