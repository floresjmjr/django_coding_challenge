from django.db import models
from movies.models import Movie

class Review(models.Model):
    class RatingEnum(models.IntegerChoices):
        TERRIBLE = 1
        DISLIKE = 2
        DECENT = 3
        GOOD = 4
        AWESOME = 5

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviewers")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    rating = models.PositiveSmallIntegerField(choices=RatingEnum.choices)
    comment = models.TextField()
    review_date = models.DateField()


    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.rating}"

