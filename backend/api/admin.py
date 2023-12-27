from django.contrib import admin
from django.db.models import Count

from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from .models import Event, Poll, PollOption, Vote, AnonUser


class PollOptionInline(NestedStackedInline):
    model = PollOption
    extra = 4
    fk_name = 'poll'


class PollInline(NestedStackedInline):
    model = Poll
    extra = 1
    fk_name = 'event'
    inlines = [PollOptionInline]


class EventAdmin(NestedModelAdmin):
    inlines = [PollInline]


class VoteAdmin(admin.ModelAdmin):
    list_display = ['poll', 'poll_option', 'total_votes']
    list_filter = ['poll', 'poll_option']
    search_fields = ['poll__name', 'poll_option__value']

    def total_votes(self, obj):
        return Vote.objects.filter(poll_option=obj.poll_option).count()

    total_votes.short_description = 'Total Votes'


class AnonUserAdmin(admin.ModelAdmin):
    list_display = ('code', 'event')  # Поля, отображаемые в списке
    list_filter = ('event',)  # Фильтры по полям
    search_fields = ('code', 'event__name')  # Поля для поиска


admin.site.register(AnonUser, AnonUserAdmin)
admin.site.register(Vote, VoteAdmin)
admin.site.register(Event, EventAdmin)
