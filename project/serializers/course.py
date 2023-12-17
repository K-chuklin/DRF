from project.models import Course
from rest_framework.serializers import ModelSerializer, IntegerField, SerializerMethodField


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseCreateSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ('name', 'preview', 'description')


class CourseListSerializer(ModelSerializer):
    subject_count = SerializerMethodField()
    is_subscribed = IntegerField(source='subscription_set.all.count', read_only=True)

    class Meta:
        model = Course
        fields = ("id", "name", "is_subscribed", "subject_count")

    def get_subject_count(self, course):
        return course.subject.count()


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
