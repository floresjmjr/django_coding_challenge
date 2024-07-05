from rest_framework.generics import ListCreateAPIView

from movies.models import Movie
from movies.serializers import MovieSerializer


class MovieListView(ListCreateAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        queryset = Movie.objects.order_by("id")
        min_runtime = self.request.query_params.get('min_runtime', None)
        max_runtime = self.request.query_params.get('max_runtime', None)
        
        if min_runtime is not None:
            queryset = queryset.filter(runtime__gte=min_runtime)

        if max_runtime is not None:
            queryset = queryset.filter(runtime__lte=max_runtime)
        
        return queryset

