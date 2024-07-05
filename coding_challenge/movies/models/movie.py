from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    runtime = models.PositiveSmallIntegerField()
    release_date = models.DateField()
    
    @property
    def runtime_formatted(self):
        hours, minutes = divmod(self.runtime, 60)
        return f"{hours}:{minutes:02d}"
    
    def __str__(self):
        return self.title