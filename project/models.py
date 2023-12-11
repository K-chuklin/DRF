from django.db import models
from users.models import User
from django.utils import timezone

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    name = models.CharField(max_length=40, verbose_name='название курса')
    preview = models.ImageField(upload_to='project/', verbose_name='превью', **NULLABLE)
    description = models.TextField(max_length=150, verbose_name='описание', **NULLABLE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='владелец', **NULLABLE)
    price = models.IntegerField(default=1000, verbose_name='Цена курса', **NULLABLE)

    def __str__(self):
        return f'Курс: {self.name}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Subject(models.Model):
    course = models.ForeignKey('Course', related_name='subject', on_delete=models.CASCADE, **NULLABLE, verbose_name='название курса')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='владелец', **NULLABLE)
    name = models.CharField(max_length=40, verbose_name='название урока')
    preview = models.ImageField(upload_to='project/', verbose_name='превью', **NULLABLE)
    description = models.TextField(max_length=150, verbose_name='описание', **NULLABLE)
    video = models.TextField(max_length=2048, verbose_name='ссылка_на_видео', **NULLABLE)

    def __str__(self):
        return f'Урок: {self.name} описание {self.description}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Payment(models.Model):
    METHODS = (
        (1, 'transfer'),
        (2, 'cash'),
    )
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE)
    payment_date = models.DateTimeField(default=timezone.now(), verbose_name='дата оплаты', **NULLABLE)
    paid_course = models.ForeignKey(Course, default=None, verbose_name='оплаченный курс', on_delete=models.CASCADE)
    payment_amount = models.IntegerField(default=None, verbose_name='сумма платежа')
    payment_method = models.CharField(choices=METHODS, default=1)

    def __str__(self):
        return f'Платеж пользователя: {self.user} за курс: {self.paid_course} на сумму {self.payment_amount}'

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'


class Subscription(models.Model):
    is_active = models.BooleanField(default=True, verbose_name="активна")
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE, **NULLABLE)
    course = models.ForeignKey(Course, verbose_name='курс', on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.user}: {self.course} {self.is_active}'

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'
        unique_together = ('user', 'course')
