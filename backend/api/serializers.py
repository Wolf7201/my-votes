from rest_framework import serializers

from .models import (
    Event,
    Poll,
    PollOption,
    AnonUser,
    Vote
)


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


class AnonUserSerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True)

    class Meta:
        model = AnonUser
        fields = ['id', 'code', 'event']


class VoteSerializer(serializers.ModelSerializer):
    poll_option = serializers.StringRelatedField()

    class Meta:
        model = Vote
        fields = ['poll', 'poll_option']


class VoteCreateSerializer(serializers.ModelSerializer):
    anon_user_code = serializers.CharField(write_only=True)

    class Meta:
        model = Vote
        fields = ['poll', 'poll_option', 'anon_user_code']

    def create(self, validated_data):
        anon_user_code = validated_data.pop('anon_user_code')
        anon_user = AnonUser.objects.get(code=anon_user_code)
        vote = Vote.objects.create(anon_user=anon_user, **validated_data)
        return vote

    def validate_anon_user_code(self, value):
        if not AnonUser.objects.filter(code=value).exists():
            raise serializers.ValidationError("Invalid anon_user_code")
        return value
