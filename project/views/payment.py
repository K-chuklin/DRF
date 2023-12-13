from project.models import Payment, Course
from django_filters.rest_framework import OrderingFilter, DjangoFilterBackend
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from project.serializers.payment import PaymentListSerializer, PaymentDetailSerializer
from project.permissions import IsOwner, IsOwnerOrStaff


class PaymentListAPIView(ListAPIView):
    serializer_class = PaymentListSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    search_fields = ('paid_course', 'payment_date', 'payment_method',)
    filter_queryset = ('payment_date',)
    permission_classes = [IsOwner]


class PaymentRetrieveAPIView(RetrieveAPIView):
    serializer_class = PaymentDetailSerializer
    queryset = Payment.objects.all()
    permission_classes = [IsOwner]


# class PaymentCreateAPIView(CreateAPIView):
#     serializer_class = PaymentDetailSerializer
#     queryset = Payment.objects.all()
#     permission_classes = [IsOwner]
#
#     # Создаем и сохраняем оплату
#     def perform_create(self, serializer, *args, **kwargs):
#         payment = serializer.save()  # получаем данные об оплате
#         payment.user = self.request.user  # сохраняем данные об оплате в профиль пользователя
#         course_pk = self.kwargs.get('pk')  # сохраняем данные об оплате в профиль курс
#         payment.course = Course.objects.get(pk=course_pk)  # получаем нужную подписку
#         payment.save()
