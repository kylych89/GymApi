from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from blog.views import *
from rest_framework.routers import DefaultRouter



router = DefaultRouter()

router.register('api/v1/aboutus', AboutUsViewSet, basename='aboutus')
router.register('api/v1/classes', ClassesViewSet, basename='classes')
router.register('api/v1/schedules', SchedulesViewSet, basename='schedules')
router.register('api/v1/contact', ContactsViewSet, basename='contact')
router.register('api/v1/user', UsersViewSet, basename='user')



schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/login/', include('djoser.urls.jwt')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='swagger'),
]

urlpatterns += router.urls
