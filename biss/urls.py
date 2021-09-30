from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('biss/', include('biss_app.api.urls')),
    path('watch/', include('watchmate_app.api.urls')),
]
