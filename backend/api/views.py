from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import AnonUser, Vote
from .models import (
    Event,
    Poll,
)
from .serializers import (
    PollSerializer,
    EventSerializer,
    VoteSerializer,
    AnonUserSerializer,
    VoteCreateSerializer
)


class EventViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class PollViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class AnonUserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AnonUser.objects.all()
    serializer_class = AnonUserSerializer

    @action(detail=True, methods=['GET'], url_path='get-vote')
    def event_info(self, request, pk=None):
        anon_user = get_object_or_404(AnonUser, code=pk)
        event = anon_user.event
        event_serializer = EventSerializer(event)

        votes = Vote.objects.filter(anon_user=anon_user)
        votes_serializer = VoteSerializer(votes, many=True)

        return Response({
            'event': event_serializer.data,
            'votes': votes_serializer.data
        })

    @action(detail=True, methods=['post'], url_path='add-vote')
    def add_vote(self, request, pk=None):
        serializer = VoteCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
