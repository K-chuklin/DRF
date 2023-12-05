from project.models import Course
from rest_framework.serializers import ModelSerializer, IntegerField, SerializerMethodField


class CourseListSerializer(ModelSerializer):

    subject_count = IntegerField(source='subject_set.all.count', read_only=True)

    class Meta:
        model = Course
        fields = ("name", "subject_count")


class CourseDetailSerializer(ModelSerializer):

    subject = SerializerMethodField()
    subject_count = SerializerMethodField()

    class Meta:
        model = Course
        fields = ('name', 'preview', "description", "subject_count", "subject")

    def get_subject_count(self, course):
        return course.subject.count()

    def get_subject(self, course):
        return [subject.name for subject in course.subject.all()]



