
from django.contrib import admin
from django.urls import path
from bikini_bottom.views import home, home_map_api, custom_map_api, facility_form_add
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('api/home-map/', home_map_api, name='home_api'),
    path('api/custom-map/', custom_map_api, name='custom_api'),
    path('facility/add/', facility_form_add, name='facility_form_add')
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)