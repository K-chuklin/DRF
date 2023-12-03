from project.models import Course
from rest_framework.serializers import ModelSerializer, IntegerField, SerializerMethodField


class CourseSerializer(ModelSerializer):
    subject_count = IntegerField(source='subject_set.all.count', read_only=True)
    # subject_count = SerializerMethodField()
    #
    # def get_subject_count(self, instance):
    #     if instance.subject_set().all().count():
    #         return instance.subject_set().all().count().Course.pk
    #     return 0

    class Meta:
        model = Course
        fields = ('name', 'preview', 'description', 'subject_count')

