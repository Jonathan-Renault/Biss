from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('biss/', include('biss_app.api.urls'), name="biss"),
    path('watch/', include('watchmate_app.api.urls')),
]
