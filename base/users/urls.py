from rest_framework import routers
from .api import PersonViewSet, UpdateFriends, FriendsViewSet
from django.urls import path

router = routers.DefaultRouter()

router.register('api/users', PersonViewSet)
router.register('api/friends', FriendsViewSet)

urlpatterns = [
    path('api/update/<str:pk>', UpdateFriends.as_view())
]


urlpatterns += router.urls
