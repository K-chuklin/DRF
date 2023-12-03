from rest_framework.viewsets import ModelViewSet
from project.models import Course
from project.serializers.course import CourseSerializer


class CourseViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
