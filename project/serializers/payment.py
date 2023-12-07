from project.models import Payment
from rest_framework.serializers import ModelSerializer


class PaymentListSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class PaymentDetailSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
