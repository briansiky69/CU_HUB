from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'CU Hub Administration'

# Add this line to include the bootstrap4 templates


urlpatterns = [
    path('admin/', admin.site.urls),
     path('', include(('event_resources.urls', 'event_resources'))),
     ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
