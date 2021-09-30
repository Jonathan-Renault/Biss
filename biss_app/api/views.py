from django.http import JsonResponse
from rest_framework import generics, mixins, status
from rest_framework.decorators import api_view

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


@api_view(['DELETE'])
def BissDeleteall(request):
    if request.method == 'DELETE':
        count = History.objects.all().delete()
        return JsonResponse({'message': '{} requests were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)
