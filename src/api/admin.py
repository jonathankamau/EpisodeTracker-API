from django.contrib import admin
from api.models import UserProfile, MySeries, LoggedEpisodes

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(MySeries)
admin.site.register(LoggedEpisodes)