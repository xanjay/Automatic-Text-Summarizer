from django.urls import path
from news import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='news_index'),
    path('file_form_upload', views.file_form_upload, name='file_form_upload'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
