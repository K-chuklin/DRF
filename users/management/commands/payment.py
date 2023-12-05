from django.core.management import BaseCommand
from users.models import User, Payment
from project.models import Course


class Command(BaseCommand):
    def handle(self, *args, **options):

        # Удаляем прошлые данные
        User.objects.all().delete()
        Course.objects.all().delete()
        Payment.objects.all().delete()

        # Создаем  пользователей
        user_test1 = User.objects.create(email="test1@testov.ru")
        user_test2 = User.objects.create(email="test2@testov.com")

        # Создаем  курсы
        course_test1 = Course.objects.create(name="Django")
        course_test2 = Course.objects.create(name="PostgrSQL")

        # Форммируем оплату
        payment_list = [
            {'user': user_test1,
             'paid_course': course_test1,
             'payment_amount': 1000,
             'payment_method': 1},
            {'user': user_test2,
             'paid_course': course_test2,
             'payment_amount': 2000,
             'payment_method': 2},
        ]

        # Записываем данные
        for payment in payment_list:
            Payment.objects.create(**payment)
