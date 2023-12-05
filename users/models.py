from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from project.models import Course


NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    phone = models.CharField(max_length=35, verbose_name='номер телефона', **NULLABLE)
    country = models.CharField(max_length=100, verbose_name='Страна', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


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
