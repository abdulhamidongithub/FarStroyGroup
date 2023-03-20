from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('asosiy/', AsosiyAPIView.as_view()),
    path('karyusellar/', KaryusellarAPIView.as_view()),
    path('kataloglar/', KataloglarAPIView.as_view()),
    path('fasadlar/', FasadlarAPIView.as_view()),
    path('bizning_uylar/', BizningUylarAPIView.as_view()),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
