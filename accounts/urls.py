from rest_framework.routers import DefaultRouter
from .views import RegisterloginView
from django.urls import path, include

router = DefaultRouter()

router.register(r'Registerlogin', RegisterloginView )

urlpatterns = [
    path("", include(router.urls))
]
