from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('profiles', views.UserViewSet)
router.register('login', views.LoginViewSet, basename='Login')

urlpatterns = [
    url(r'', include(router.urls))
]