from django.conf.urls import include
from django.urls import path
from rest_framework import routers

from .app_settings import ACCEPT_INVITE_URL, API_BASE_URL
from .views import InvitationViewSet, accept_invitation

router = routers.SimpleRouter()
router.register(r'{0}'.format(API_BASE_URL), InvitationViewSet)

invitations_patterns = (
    [
        path(
            '{0}/{1}/<key>)/'.format(
                API_BASE_URL, ACCEPT_INVITE_URL
            ),
            accept_invitation,
            name='accept-invite'
        ),
    ],
    'invitations'
)

urlpatterns = router.urls + [
    path('', include(invitations_patterns)),
]
