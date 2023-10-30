from django.contrib import admin
from django.urls import path, include
from bikini_bottom.views import home, home_map_api, custom_map_api, facility_form_add, facility_form_update, facility_form_delete, facility_list
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('api/home-map/', home_map_api, name='home_api'),
    path('api/custom-map/', custom_map_api, name='custom_api'),
    path('facility/', facility_list, name='facility_list'),
    path('facility/add/', facility_form_add, name='facility_form_add'),
    path('facility/update/<int:pk>/', facility_form_update, name='facility_form_update'),
    path('facility/delete/<int:pk>/', facility_form_delete, name='facility_form_delete'),

    # Sistem Authentication
    path('', include('django.contrib.auth.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)