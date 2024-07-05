from rest_framework.generics import ListCreateAPIView

from reviews.models import Review
from reviews.serializers import ReviewSerializer


class ReviewListView(ListCreateAPIView):
    queryset = Review.objects.order_by("id")
    serializer_class = ReviewSerializer
