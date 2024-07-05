from rest_framework import serializers
from movies.models import Movie
from reviews.serializers import ReviewSerializer
from django.db.models import Avg

class MovieSerializer(serializers.ModelSerializer):

    reviewers = ReviewSerializer(many=True, read_only=True)
    avg_rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
            "runtime",
            "release_date",
            "runtime_formatted",
            "avg_rating",
            "reviewers",
        )

    def get_avg_rating(self, obj):
        avg_rating = obj.reviewers.aggregate(Avg('rating'))['rating__avg']
        return avg_rating if avg_rating is not None else 0.0
    
    