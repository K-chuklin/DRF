from project.apps import ProjectConfig
from rest_framework.routers import DefaultRouter
from project.views.course import CourseViewSet
from project.views.payment import PaymentListAPIView, PaymentRetrieveAPIView
from project.views.subject import SubjectCreateAPIView, SubjectListAPIView, SubjectRetrieveAPIView, \
    SubjectUpdateAPIView, SubjectDestroyPIView
from django.urls import path


app_name = ProjectConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
    path('subject/create/', SubjectCreateAPIView.as_view(), name='subject-create'),
    path('subjects/', SubjectListAPIView.as_view(), name='subject-list'),
    path('subject/<int:pk>/', SubjectRetrieveAPIView.as_view(), name='subject-get'),
    path('subject/update/<int:pk>/', SubjectUpdateAPIView.as_view(), name='subject-update'),
    path('subject/delete/<int:pk>/', SubjectDestroyPIView.as_view(), name='subject-delete'),

    path('payment/', PaymentListAPIView.as_view(), name='payment_list'),
    path('payment/<int:pk>/', PaymentRetrieveAPIView.as_view(), name='payment_retrieve'),
] + router.urls
