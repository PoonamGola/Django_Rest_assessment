from django.urls import path, include
from rest_framework import routers
from .views import ArtistViewSet, WorkViewSet, RegisterAPIView

router = routers.DefaultRouter()
router.register(r'artists', ArtistViewSet)
router.register(r'works', WorkViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterAPIView.as_view(), name='register'),
]
