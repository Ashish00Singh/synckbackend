# from django.contrib import admin
from django.urls import path, include
from .views import AdditionalViewsSet, CovrageViewsSet
from rest_framework.routers import DefaultRouter
# from api import views
router = DefaultRouter()

router.register(r'AdditionalPlan', AdditionalViewsSet)
router.register(r'CovragePlan', CovrageViewsSet)

urlpatterns = [
    path('', include(router.urls)),
]