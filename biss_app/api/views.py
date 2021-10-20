from django.http import JsonResponse
from rest_framework import generics, mixins, status
from rest_framework.decorators import api_view

from biss_app.api.serializers import HistorySerializer
from biss_app.models import History


class BissList(generics.ListAPIView):
    """
    List all history of :view:`biss_app.BissList`
    """
    queryset = History.objects.all()
    serializer_class = HistorySerializer


class BissCreate(generics.CreateAPIView):
    """
    In the class BissCreate
    """
    serializer_class = HistorySerializer

    def perform_create(self, serializer):
        """
        Post a request of Bissectile year.
        Return an bool.
        Save in :model:`biss_app.History`.
        """
        year = self.kwargs.get('pk')

        if (year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0):
            res = True
        else:
            res = False

        serializer.save(req=year, res=res)


@api_view(['DELETE'])
def BissDeleteall(request):
    """
    Delete all history
    """
    if request.method == 'DELETE':
        count = History.objects.all().delete()
        return JsonResponse({'message': '{} requests were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)
