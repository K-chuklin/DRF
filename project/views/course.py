from rest_framework.viewsets import ModelViewSet

from project.models import Course
from project.permissions import IsOwnerOrStaff, IsOwner
from project.serializers.course import CourseDetailSerializer, CourseListSerializer, CourseSerializer, \
    CourseCreateSerializer
from rest_framework.permissions import IsAuthenticated


class CourseViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsOwnerOrStaff]
    serializers = {
        'list': CourseListSerializer,
        'retrieve': CourseDetailSerializer,
        'create': CourseCreateSerializer
    }

    # Если пользователь - владелец, он может создавать курс
    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()

    # Фильтрация представлений по условиям
    def get_permissions(self):

        if self.action == 'list':
            permission_classes = [IsOwnerOrStaff]
        elif self.action == 'retrieve':
            permission_classes = [IsOwnerOrStaff]
        elif self.action == 'create':
            permission_classes = [IsOwner]
        elif self.action == 'update':
            permission_classes = [IsOwnerOrStaff]
        elif self.action == 'destroy':
            permission_classes = [IsOwner]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

