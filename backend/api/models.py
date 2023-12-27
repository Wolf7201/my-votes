from django.db import models
from datetime import datetime

STATUS_CHOICES = (
    ('waiting', 'Ожидание'),
    ('draft', 'Черновик'),
    ('voting', 'Голосование'),
    ('completed', 'Завершен'),
)


class BaseEvent(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Название',
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='waiting',
        verbose_name='Статус',
    )
    start_date = models.DateTimeField(
        verbose_name='Время начала',
        default=datetime.now,
    )

    class Meta:
        abstract = True
        ordering = ('id',)


class Event(BaseEvent):

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'
        default_related_name = 'events'


class Poll(BaseEvent):
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        verbose_name='Мероприятие'
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'
        default_related_name = 'polls'


class PollOption(models.Model):
    value = models.CharField(
        max_length=255,
        verbose_name='Значение',
    )
    poll = models.ForeignKey(
        Poll,
        on_delete=models.CASCADE,
        verbose_name='Опрос',
    )

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответа'
        default_related_name = 'poll_options'


class AnonUser(models.Model):
    code = models.CharField(
        max_length=4,
        verbose_name='Код',
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        verbose_name='Мероприятие',
    )

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'Анонимный пользователь'
        verbose_name_plural = 'Анонимные пользователи'
        default_related_name = 'anon_users'


class Vote(models.Model):
    poll = models.ForeignKey(
        Poll,
        on_delete=models.CASCADE,
        verbose_name='Опрос',
    )
    poll_option = models.ForeignKey(
        PollOption,
        on_delete=models.CASCADE,
        verbose_name='Вариант ответа',
    )
    anon_user = models.ForeignKey(
        AnonUser,
        on_delete=models.CASCADE,
        verbose_name='Анонимный пользователь',
    )

    def __str__(self):
        return f"Vote for {self.poll_option} in {self.poll}"

    class Meta:
        verbose_name = 'Голос'
        verbose_name_plural = 'Голоса'
        default_related_name = 'votes'
