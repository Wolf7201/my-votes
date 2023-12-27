from rest_framework import serializers
from .models import (Event, Poll, PollOption)


class PollOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollOption
        fields = ('id', 'value')


class PollSerializer(serializers.ModelSerializer):
    poll_options = PollOptionSerializer(many=True)

    class Meta:
        model = Poll
        fields = ('id', 'name', 'status', 'poll_options')


class EventSerializer(serializers.ModelSerializer):
    polls = PollSerializer(many=True)

    class Meta:
        model = Event
        fields = ('id', 'name', 'status', 'polls',)
