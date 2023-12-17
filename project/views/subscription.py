from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, UpdateAPIView
from rest_framework.serializers import ModelSerializer
from rest_framework.relations import SlugRelatedField
from project.models import Course, Subscription
from project.serializers.subscription import SubscriptionSerializer
from rest_framework.permissions import IsAuthenticated


class SubscriptionListSerializer(ModelSerializer):
    # Меняем id курса на его название

    course = SlugRelatedField(slug_field="name", queryset=Course.objects.all())
    # permission_classes = [IsAuthenticated]

    class Meta:
        model = Subscription
        fields = "__all__"


class SubscriptionCreateAPIView(CreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    # permission_classes = [IsAuthenticated]

    # Создаем и сохраняем подписку
    def perform_create(self, serializer, *args, **kwargs):
        subscription = serializer.save()  # получаем данные подписки
        subscription.user = self.request.user  # сохраняем данные о подписке в профиль пользователя
        course_pk = self.kwargs.get('pk')  # сохраняем данные о подписке в профиль курс
        subscription.course = Course.objects.get(pk=course_pk)  # получаем нужную подписку
        subscription.save()


class SubscriptionDestroyAPIView(DestroyAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    # permission_classes = [IsAuthenticated]


class SubscriptionListAPIView(ListAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    # permission_classes = [IsAuthenticated]


class SubscriptionUpdateAPIView(UpdateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    # permission_classes = [IsAuthenticated]