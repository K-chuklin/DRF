from project.models import Subject
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = "__all__"
