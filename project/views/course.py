from rest_framework.viewsets import ModelViewSet
from users.models import Payment
from project.serializers.course import CourseDetailSerializer


class CourseViewSet(ModelViewSet):
    serializer_class = CourseDetailSerializer
    queryset = Course.objects.all()
