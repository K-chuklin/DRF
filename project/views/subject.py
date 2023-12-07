from rest_framework import generics
from project.models import Subject
from project.permissions import IsOwner, IsOwnerOrStaff
from project.serializers.subject import SubjectSerializer
from rest_framework.permissions import IsAuthenticated


class SubjectCreateAPIView(generics.CreateAPIView):
    serializer_class = SubjectSerializer
    permission_classes = [IsOwner]


class SubjectListAPIView(generics.ListAPIView):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
    permission_classes = [IsAuthenticated]


class SubjectRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
    permission_classes = [IsAuthenticated]


class SubjectUpdateAPIView(generics.UpdateAPIView):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
    permission_classes = [IsOwnerOrStaff]


class SubjectDestroyPIView(generics.DestroyAPIView):
    queryset = Subject.objects.all()
    permission_classes = [IsOwner]
