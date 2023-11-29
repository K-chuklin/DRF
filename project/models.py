from users.models import NULLABLE
from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=40, verbose_name='название')
    preview = models.ImageField(upload_to='project/', verbose_name='превью', **NULLABLE)
    description = models.TextField(max_length='150', verbose_name='описание', **NULLABLE)

    def __str__(self):
        return f'Курс: {self.name}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Subject(models.Model):
    name = models.CharField(max_length=40, verbose_name='название')
    preview = models.ImageField(upload_to='project/', verbose_name='превью', **NULLABLE)
    description = models.TextField(max_length='150', verbose_name='описание', **NULLABLE)
    video = models.TextField(max_length=2048, verbose_name='ссылка_на_видео', **NULLABLE)

    def __str__(self):
        return f'Урок: {self.name}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
