from project.apps import ProjectConfig
from rest_framework.routers import DefaultRouter
from project.views import CourseViewSet, SubjectCreateAPIView, SubjectListAPIView, SubjectRetrieveAPIView, \
    SubjectUpdateAPIView, SubjectDestroyPIView
from django.urls import path


app_name = ProjectConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
    path('subject/create/', SubjectCreateAPIView.as_view(), name='subject-create'),
    path('subject/', SubjectListAPIView.as_view(), name='subject-list'),
    path('subject/<int:pk>/', SubjectRetrieveAPIView.as_view(), name='subject-get'),
    path('subject/update/<int:pk>/', SubjectUpdateAPIView.as_view(), name='subject-update'),
    path('subject/delete/<int:pk>/', SubjectDestroyPIView.as_view(), name='subject-delete'),
] + router.urls
