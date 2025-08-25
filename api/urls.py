# from django.contrib import admin
from django.urls import path, include
from .views import SynckHealthViewSet
from rest_framework.routers import DefaultRouter
# from api import views
router = DefaultRouter()

router.register(r'synckHealtPlan', SynckHealthViewSet)

urlpatterns = [
    path('', include(router.urls)),
]