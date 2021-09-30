from django.urls import path
from biss_app.api.views import BissList, BissCreate

urlpatterns = [
    path('', BissList.as_view(), name='biss'),
    path('<int:pk>', BissCreate.as_view(), name='biss'),
]
