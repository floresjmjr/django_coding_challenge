from django.urls import path

from movies.views import MovieListView
from movies.views import MovieDetailsView


urlpatterns = [
    path("", MovieListView.as_view(), name="MovieListView"),
    path("<int:id>", MovieDetailsView.as_view(), name="MovieDetailsView"),
]
