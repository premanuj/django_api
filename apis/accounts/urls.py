from rest_framework import routers
from apis.accounts.views import UserAPIView

router = routers.DefaultRouter()
router.register('users', UserAPIView)
urlpatterns = router.urls