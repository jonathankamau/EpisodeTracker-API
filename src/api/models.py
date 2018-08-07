from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BaseModel(models.Model):
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    class Meta:
        abstract = True

class UserProfile(BaseModel, User):
    profile_image = models.ImageField(blank=True)

    class Meta:
        db_table = 'user_profile'

    def __str__(self):
        return "User: {}".format(self.user.username)

class MySeries(BaseModel):
    series_id = models.CharField(primary_key=True, max_length=50)
    series_image = models.CharField(max_length=50)
    description = models.TextField(blank=False)
    watch_status = models.CharField(max_length=50)
    series_name = models.CharField(max_length=50)
    users = models.ManyToManyField(
        User,
        through='LoggedEpisodes',
        through_fields=('series', 'user'),
    )

    class Meta:
        db_table = 'my_series'

    def __str__(self):
        return "My Series: {}".format(self.series_name)

class LoggedEpisodes(BaseModel):
    season_id = models.CharField(max_length=50)
    episode_id = models.CharField(max_length=50)
    series = models.ForeignKey(MySeries, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'logged_episodes'

    def __str__(self):
        return "Logged Episodes: {}".format(self.id)
