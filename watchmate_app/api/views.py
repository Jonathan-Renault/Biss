from rest_framework import generics

from watchmate_app.models import WatchM, PlatformM, ReviewM

from watchmate_app.api.serializers import WatchSerializer, PlatformSerializer, ReviewSerializer


class WatchList(generics.ListCreateAPIView):
    queryset = WatchM.objects.all()
    serializer_class = WatchSerializer


class WatchDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = WatchM.objects.all()
    serializer_class = WatchSerializer


class PlatformList(generics.ListCreateAPIView):
    queryset = PlatformM.objects.all()
    serializer_class = PlatformSerializer


class PlatformDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlatformM.objects.all()
    serializer_class = PlatformSerializer


class WatchByPlatform(generics.ListAPIView):
    serializer_class = PlatformSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return PlatformM.objects.filter(platform=pk)


class ReviewList(generics.ListCreateAPIView):
    queryset = ReviewM.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReviewM.objects.all()
    serializer_class = ReviewSerializer


class ReviewByWatch(generics.ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return ReviewM.objects.filter(watch=pk)
