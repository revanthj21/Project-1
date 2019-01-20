from django.conf.urls import url, include
from Assignment2.weather.views import WeatherViewSet, WeatherForecastViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='API')

router = DefaultRouter()
router.register(r'historical', WeatherViewSet)
router.register(r'forecast', WeatherForecastViewSet)

urlpatterns = [
    url(r'^swagger/', schema_view),
]
urlpatterns += router.urls