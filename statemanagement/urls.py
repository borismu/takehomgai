from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import StateContainerViewset

router = DefaultRouter()
router.register(r'statecontainers', StateContainerViewset)

urlpatterns = [
    path('', include(router.urls)),
]