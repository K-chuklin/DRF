from project.models import Payment
from rest_framework.serializers import ModelSerializer


class PaymentListSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = ('user', 'paid_course')


class PaymentDetailSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class PaymentCreateSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = ('paid_course', 'payment_amount', 'payment_method')
