from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Weather
from .serializers import DataSerializer
from rest_framework import mixins, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from datetime import timedelta, datetime
from django.core.serializers import serialize

class WeatherViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
	queryset = Weather.objects.all()
	serializer_class = DataSerializer

	def create(self, request):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		return Response(serializer.data, status=status.HTTP_201_CREATED)

	def destroy(self, request, pk=None):
		queryset = Weather.objects.all()
		data = get_object_or_404(queryset, DATE=pk)
		serializer = self.get_serializer(data, many=False)
		self.perform_destroy(data)
		return Response(status=status.HTTP_204_NO_CONTENT)

	def list(self, request):
		queryset = Weather.objects.all()
		serializer = self.get_serializer(queryset, many=True)
		return Response(serializer.data)
		##return render(request,'public/index.html',{'op':serializer.data})

	def retrieve(self, request, pk=None):
		queryset = Weather.objects.all()
		data = get_object_or_404(queryset, DATE=pk)
		serializer = self.get_serializer(data, many=False)
		return Response(serializer.data)


class WeatherForecastViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
	queryset = Weather.objects.all()
	serializer_class = DataSerializer

	def retrieve(self, request, pk=None):
		startDate = datetime(int(pk[:4]), int(pk[4:6]), int(pk[6:]))
		response = []
		for n in range(7):
			currDate = (startDate + timedelta(days=n)).strftime("%Y%m%d")
			serializer = self.get_serializer(Weather.objects.all().filter(DATE=currDate), many=True)
			if len(serializer.data)==0:
				serializer = self.get_serializer(Weather.objects.all().filter(DATE='2014'+currDate[4:]), many=True)
			response.append(serializer.data[0])
		return Response(response)
