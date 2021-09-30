from django.urls import path
from biss_app.api.views import BissList, BissCreate, BissDeleteall

urlpatterns = [
    path('', BissList.as_view()),
    path('<int:pk>/', BissCreate.as_view()),
    path('delete/', BissDeleteall),
]
