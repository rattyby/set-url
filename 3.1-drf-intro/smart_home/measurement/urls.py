from django.urls import path
from .views import MeasurementsView, SensorView


urlpatterns = [
    path('sensors/', SensorView.as_view({'get': 'list'})),
    path('sensors/<pk>/', SensorView.as_view({'get': 'retrieve'})),
    path('measurements/', MeasurementsView.as_view({'get': 'list'})),
    path('measurements/', MeasurementsView.as_view({'get': 'retrieve'})),
]
