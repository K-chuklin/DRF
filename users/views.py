from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from project.permissions import IsOwnerOrStaff, IsOwner
from users.models import User
from users.serializers import UserSerializer, MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    # Фильтрация представлений по условиям
    def get_permissions(self):

        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        elif self.action == 'retrieve':
            permission_classes = [IsAuthenticated]
        elif self.action == 'update':
            permission_classes = [IsOwnerOrStaff]
        elif self.action == 'destroy':
            permission_classes = [IsOwner]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
