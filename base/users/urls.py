from rest_framework import routers
from .api import PersonViewSet

router = routers.DefaultRouter()

router.register('api/users', PersonViewSet)

urlpatterns = router.urls