from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('users.urls')),
    url(r'^', include('tasks.urls')),
    url(r'^', include('clients.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

