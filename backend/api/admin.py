from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from .models import Event, Poll, PollOption


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


admin.site.register(Event, EventAdmin)
