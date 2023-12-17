import os
import stripe

from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from project.models import Payment
from project.permissions import IsOwner
from project.serializers.payment import PaymentListSerializer, PaymentDetailSerializer, PaymentCreateSerializer


class PaymentListAPIView(ListAPIView):
    serializer_class = PaymentListSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course', 'date', 'method',)
    ordering_fields = ("date",)
    # permission_classes = [IsOwner]


class PaymentRetrieveAPIView(RetrieveAPIView):
    serializer_class = PaymentDetailSerializer
    queryset = Payment.objects.all()
    # permission_classes = [IsOwner]


class PaymentCreateAPIView(CreateAPIView):
    serializer_class = PaymentCreateSerializer
    queryset = Payment.objects.all()
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """Создаем платеж"""

        stripe.api_key = os.getenv("STRIPE_API_KEY")

        course_id = request.data.get("course")

        response = stripe.PaymentIntent.create(
            amount=2000,
            currency="usd",
            automatic_payment_methods={"enabled": True, "allow_redirects": "never"},
        )

        stripe.PaymentIntent.confirm(
            response.id,
            payment_method="pm_card_visa",
        )

        user = self.request.user

        data = {"user": user.id, "course": course_id, "is_confirmed": True}

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



