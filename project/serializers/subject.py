from project.models import Subject
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from project.validators import YouTubeLinksOnly


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = "__all__"
        validators = [YouTubeLinksOnly(field='description' and 'video')]
