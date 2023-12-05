from users.models import Payment
from django_filters.rest_framework import OrderingFilter, DjangoFilterBackend
from rest_framework.generics import ListAPIView, RetrieveAPIView
from project.serializers.payment import PaymentListSerializer, PaymentDetailSerializer


class PaymentListAPIView(ListAPIView):
    serializer_class = PaymentListSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course', 'lesson', 'payment_choice',)
    ordering_fields = ('date',)


class PaymentRetrieveAPIView(RetrieveAPIView):
    serializer_class = PaymentDetailSerializer
    queryset = Payment.objects.all()
