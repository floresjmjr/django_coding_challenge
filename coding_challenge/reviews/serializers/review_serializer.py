from rest_framework import serializers

from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = (
            "name",
            "rating",
            "comment",
            "review_date"
        )
    
    def get_name(self, obj):
        return f"{obj.first_name.capitalize()} {obj.last_name.capitalize()}"