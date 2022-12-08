from django.urls import path, include
from rest_framework.authtoken import views
from api.views import PostModelViewSet, GroupModelViewSet, CommentModelViewSet
from rest_framework import routers


v1_router = routers.DefaultRouter()
v1_router.register(r'posts', PostModelViewSet)
v1_router.register(r'groups', GroupModelViewSet)
v1_router.register(r'posts/(?P<post_id>\d+)/comments',
                   CommentModelViewSet, basename='comments')

app_name = 'posts'

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include(v1_router.urls)),

]
