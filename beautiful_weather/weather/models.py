import requests

from django.db import models
from django.conf import settings


class Request(models.Model):
    city = models.CharField('Город', max_length=100, blank=True, null=True)
    created = models.DateTimeField('Время создания', auto_now_add=True)
    result = models.TextField('Результат проверки погоды', blank=True)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-created']

    def __str__(self):
        return str(self.id)

    def check_weather(self):
        params = {
            'q': self.city,
            'appid': settings.WEATHER_API_KEY,
            'mode': 'html',
        }
        response = requests.get(settings.WEATHER_API_URL, params)
        response.raise_for_status()
        self.result = str(response.text)
        self.save()
