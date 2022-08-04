from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets

from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer


class MeasurementsView(viewsets.ViewSet):
    def list(self, request):
        queryset = Measurement.objects.all()
        serializer = MeasurementSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        # sensor = Sensor.objects.get(id=request.data['sensor'])
        # sensor_ser = SensorSerializer(instance=sensor, data={'name': sensor.name, 'description': sensor.description})
        # if sensor_ser.is_valid():
        serializer = MeasurementSerializer(data={'id_sensor': request.data['sensor'],
                                                 'temperature': request.data['temperature']})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data)
        return Response(serializer.errors)
        # return Response(sensor_ser.errors)


class SensorView(viewsets.ViewSet):
    def list(self, request):
        queryset = Sensor.objects.all()
        serializer = SensorSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Sensor.objects.all()
        sensor = get_object_or_404(queryset, pk=pk)
        serializer = SensorDetailSerializer(sensor)
        return Response(serializer.data)

    def post(self, request):
        serializer = SensorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data)
        return Response(serializer.errors)
