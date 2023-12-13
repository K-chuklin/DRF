from project.apps import ProjectConfig
from rest_framework.routers import DefaultRouter
from project.views.course import CourseViewSet, SubscriptionCreateAPIView, SubscriptionDestroyAPIView
from project.views.payment import PaymentListAPIView, PaymentRetrieveAPIView
from project.views.subject import SubjectCreateAPIView, SubjectListAPIView, SubjectRetrieveAPIView, \
    SubjectUpdateAPIView, SubjectDestroyPIView
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


app_name = ProjectConfig.name

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="DRF_homeworks API description",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="admin@admin.pro"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


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
    path('subscribe/<int:pk>/', SubscriptionCreateAPIView.as_view(), name='subscribe-create'),
    path('subscribe/delete/<int:pk>/', SubscriptionDestroyAPIView.as_view(), name='subscribe-delete'),

    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + router.urls
