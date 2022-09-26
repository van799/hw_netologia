from django.urls import path

from measurement.views import SensorView, MeasurementView, SensorRetrieveUpdate



urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensor/<pk>/', SensorRetrieveUpdate.as_view()),
    path('sensor/', SensorView.as_view()),
    path('measurement/', MeasurementView.as_view()),

]
