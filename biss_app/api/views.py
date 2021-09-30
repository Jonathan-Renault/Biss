from rest_framework import generics

from biss_app.api.serializers import HistorySerializer
from biss_app.models import History


class BissList(generics.ListAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializer


class BissCreate(generics.CreateAPIView):
    serializer_class = HistorySerializer

    def perform_create(self, serializer):
        year = self.kwargs.get('pk')

        if (year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0):
            res = True
        else:
            res = False

        serializer.save(req=year, res=res)
