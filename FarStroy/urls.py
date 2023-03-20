from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from asosiy.views import *
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="FarStroyGroup web-API",
      default_version='v1',
      description="FarStroyGroup korxonasi web-dasturi uchun qurilgan web-API",
      contact=openapi.Contact(email="1997abdulhamid@gmail.com"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('asosiy/', AsosiyAPIView.as_view()),
    path('karyusellar/', KaryusellarAPIView.as_view()),
    path('kataloglar/', KataloglarAPIView.as_view()),
    path('fasadlar/', FasadlarAPIView.as_view()),
    path('bizning_uylar/', BizningUylarAPIView.as_view()),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

