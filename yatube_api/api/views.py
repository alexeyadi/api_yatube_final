from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from posts.models import Post, Group
from .serializers import CommentSerializer, GroupSerializer, PostSerializer

from .permissions import AuthorOrReadOnly
from rest_framework import permissions
from django.shortcuts import get_object_or_404


class PostModelViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthorOrReadOnly, permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupModelViewSet(ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentModelViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (AuthorOrReadOnly, permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user, post_id=self.kwargs['post_id']
        )

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        return post.comments
