from django.db import models

# Create your models here.

class BaseModel(models.Model):
    date_created = models.DateField(max_length=50)
    date_modified = models.DateField(max_length=50)

class User(BaseModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_image = models.ImageField(blank=True)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return "User: {}".format(self.first_name)

class MySeries(BaseModel):
    series_id = models.CharField(max_length=50)
    user_id = models.IntegerField()
    series_image = models.CharField(max_length=50)
    description = models.TextField(blank=False)
    watch_status = models.CharField(max_length=50)
    series_name = models.CharField(max_length=50)

    def __str__(self):
        return "My Series: {}".format(self.series_name)

class LoggedEpisodes(BaseModel):
    series_id = models.CharField(max_length=50)
    season_id = models.CharField(max_length=50)
    episode_id = models.CharField(max_length=50)
    user_id = models.IntegerField()

    def __str__(self):
        return "Logged Episodes: {}".format(self.id)
