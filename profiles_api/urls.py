from django.urls import path, include
from profiles_api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register('hello-viewset', views.HelloWorldViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.ProfileFeedItemViewSet)

urlpatterns = [
    # path('hello-view/', views.helloworld.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
]
