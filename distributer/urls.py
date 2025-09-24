from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import distributorView

router = DefaultRouter()
router.register(r'distubter', distributorView, basename="distubter")

urlpatterns = [
    path('', include(router.urls)),
]

