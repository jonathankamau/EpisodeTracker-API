from api.models import UserProfile, MySeries, LoggedEpisodes
from rest_framework.validators import UniqueTogetherValidator
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    def create(self, user_details):
        user = UserProfile.objects.create(
            first_name = user_details['first_name'],
            last_name = user_details['last_name'],
            username = user_details['username'],
            email = user_details['email']
            )

        user.set_password(user_details['password'])
        user.save()
        return user

    class Meta:
        model = UserProfile
        validators = [ UniqueTogetherValidator(queryset=UserProfile.objects.all(),
            fields = ('first_name', 'last_name', 'username', 'email', 'password')
        )]
        fields = ('first_name', 'last_name', 'username', 'email', 'password')


class MySeriesSerializer(serializers.ModelSerializer):


    class Meta:
        model = MySeries
        fields = ('series_id', 'series_name','series_image', 'description', 'watch_status')

class LoggedEpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoggedEpisodes
        fields = ('season_id', 'episode_id', 'series')
