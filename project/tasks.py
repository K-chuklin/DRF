from celery import shared_task
from models import Course, Subscription


@shared_task
def check_update(pk):
    course = Course.objects.get(pk=pk)

    subscriptions = Subscription.objects.filter(course=pk)

    if subscriptions:
        for subscription in subscriptions:
            print(f'Привет, {subscription.user}! Автор курса "{course.course_title}" внёс изминения!')
