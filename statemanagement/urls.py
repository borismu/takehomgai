from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import StateContainerViewset, StateChange, stateChangeView

router = DefaultRouter()
router.register(r'statecontainers', StateContainerViewset)

urlpatterns = [
    path("statechange/", StateChange.as_view()),
    path("schange/", stateChangeView),
    path("", include(router.urls)),
]