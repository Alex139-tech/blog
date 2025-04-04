from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('curd/', include('curd.urls')),  # Including blog app URLs
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
