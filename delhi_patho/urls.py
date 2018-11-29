
from django.contrib import admin
from django.urls import path
from report import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404


urlpatterns = [
    path('',views.index),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

