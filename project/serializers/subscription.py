from project.models import Subscription
from rest_framework.serializers import ModelSerializer


class SubscriptionSerializer(ModelSerializer):

    class Meta:
        model = Subscription
        fields = '__all__'
