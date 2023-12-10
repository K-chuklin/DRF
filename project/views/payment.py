from project.models import Payment
from django_filters.rest_framework import OrderingFilter, DjangoFilterBackend
from rest_framework.generics import ListAPIView, RetrieveAPIView
from project.serializers.payment import PaymentListSerializer, PaymentDetailSerializer
from project.permissions import IsOwner, IsOwnerOrStaff


class PaymentListAPIView(ListAPIView):
    serializer_class = PaymentListSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    search_fields = ('paid_course', 'payment_date', 'payment_method',)
    filter_queryset = ('payment_date',)
    permission_classes = [IsOwnerOrStaff]


class PaymentRetrieveAPIView(RetrieveAPIView):
    serializer_class = PaymentDetailSerializer
    queryset = Payment.objects.all()
    permission_classes = [IsOwner]
