
from django.contrib import admin
from django.urls import path
from bikini_bottom.views import home, home_map_api, custom_map_api  # Import custom_map_api
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('api/home-map/', home_map_api),
    path('api/custom-map/', custom_map_api, name='custom_api'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
