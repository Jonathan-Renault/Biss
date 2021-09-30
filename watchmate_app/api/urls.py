
from django.urls import path

from watchmate_app.api.views import WatchList, WatchDetail, PlatformList, PlatformDetail, ReviewList, ReviewDetail, \
    ReviewByWatch

urlpatterns = [
    path('', WatchList.as_view()),
    path('<int:pk>/', WatchDetail.as_view()),

    path('platform/', PlatformList.as_view()),
    path('platform/<int:pk>/', PlatformDetail.as_view()),

    path('review/', ReviewList.as_view()),
    path('review/<int:pk>/', ReviewDetail.as_view()),
    path('<int:pk>/review/', ReviewByWatch.as_view()),
]
