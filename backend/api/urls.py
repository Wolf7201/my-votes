from django.urls import path, include
from rest_framework import routers
from .views import EventViewSet, PollViewSet

app_name = 'api'

router = routers.DefaultRouter()

router.register('events', EventViewSet, basename='events')
router.register('polls', PollViewSet, basename='polls')

urlpatterns = [
    path('', include(router.urls)),
]
