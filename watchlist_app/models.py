from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class StreamPlatform(models.Model):
    name = models.CharField(max_length=255)
    about = models.TextField(max_length=255)
    webside = models.URLField(max_length=100)

    def __str__(self):
        return self.name

class WatchList(models.Model):
    stream = models.ForeignKey(StreamPlatform, related_name='watchlist',on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    storyline =models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class Review(models.Model):
    watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name='review')
    rating = models.PositiveBigIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description =models.CharField(max_length=255, null=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    def __str__(self) :
        return str(self.rating)+ " "+ self.watchlist.title
