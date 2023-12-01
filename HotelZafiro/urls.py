from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
#from django.contrib.auth.views import login, logout_then_login


urlpatterns = [
    path('', include('Hotel.urls')),
    path('', include('reservacion.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

]
#urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


