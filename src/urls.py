"""EpisodeTracker URL Configuration
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static
from rest_framework import routers
from api.views.register_view import RegisterUser
import settings

api_router = routers.DefaultRouter(trailing_slash=False)
api_router.register(r'register', RegisterUser, 'register')

urlpatterns = [
    url(r'^api/v1/', include(api_router.urls)),
    url('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
