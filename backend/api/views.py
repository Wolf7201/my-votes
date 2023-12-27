from rest_framework import viewsets
from .serializers import EventSerializer, PollSerializer

from .models import (
    Event,
    Poll,
)


class EventViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class PollViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
