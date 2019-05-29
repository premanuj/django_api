from rest_framework import routers
from apis.accounts.views import UserAPIView

router = routers.SimpleRouter()
router.register('users', UserAPIView)
urlpatterns = router.urls