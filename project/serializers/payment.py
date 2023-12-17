from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer
from project.models import Payment
from users.models import User


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"


class PaymentListSerializer(ModelSerializer):
    user = SlugRelatedField(slug_field='email', queryset=User.objects.all())

    class Meta:
        model = Payment
        fields = ('user', 'course')


class PaymentDetailSerializer(ModelSerializer):
    user = SlugRelatedField(slug_field='email', queryset=User.objects.all())

    class Meta:
        model = Payment
        fields = '__all__'


class PaymentCreateSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = ('course', 'amount', 'method')
