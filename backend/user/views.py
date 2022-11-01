from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import User
from post.models import Post
from .permissions import IsUserOrReadOnly




from .serializers import UserSerializer, UserFollowSerializer, OnlyFollowSerializer, RepresentationUserSerializer, CreateUserSerializer
from post.serializers import PostSerializer


class ListFollowersUserView(ListAPIView):
    """
        Get a List of all followers

        Get a List of all the users following the logged-in user.
    """
    permission_classes = [
        IsAuthenticated
    ]
    def get_queryset(self):
        return User.objects.filter(is_following=self.request.user)
    serializer_class = UserFollowSerializer


class ListPeopleTheUserFollowsView(GenericAPIView):
    """
        Get a List of all followed users

        Get a List of all the users the logged-in user is following.
    """
    permission_classes = [
        IsAuthenticated
    ]
    def get(self, request, *args, **kwargs):
        user = User.objects.filter(id=request.user.id)
        serializer = OnlyFollowSerializer(user, many=True)
        return Response(serializer.data[0]["is_following"])


class ListPostsOfFollowedPeopleView(GenericAPIView):
    """
        Get the followed peoples posts

        Get a List of all the posts of users that are being followed by the logged-in user.
    """
    permission_classes = [
        IsAuthenticated
    ]
    def get(self, request, *args, **kwargs):
        user = self.request.user
        following = user.is_following.all()
        serializer = UserSerializer(following, many=True)
        data = serializer.data
        ids = []
        for person in data:
            ids.append(person["id"])
        posts = Post.objects.filter(owner__in=ids)
        serializer = PostSerializer(posts, many=True)

        return Response(serializer.data)


class ToggleFollowView(GenericAPIView):
    """
    patch:
    Follow / Unfollow

    Toggle between "following" or "not following" a certain user, by passing the user-id into the url.
    This will add the chosen users user-id to the logged-in user's "is_following" list, or remove them
    if they are already on the list.
    """
    permission_classes = [
        IsAuthenticated
    ]
    queryset = User
    serializer_class = UserFollowSerializer
    lookup_url_kwarg = 'userID'

    def patch(self, request, *args, **kwargs):
        me = self.request.user
        person = self.get_object()
        me_follows_person = person in me.is_following.all()
        if me_follows_person:
            me.is_following.remove(person)
        else:
            me.is_following.add(person)

        return Response(self.get_serializer(me).data)


class ListCreateUserView(ListCreateAPIView):
    """
    get:
    Get a List of all users

    Get a List of all users.

    post:
    Create a new user

    Create a new user.
    """
    queryset = User.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateUserSerializer
        return RepresentationUserSerializer


class RetrieveUpdateDestroyUserAPIView(RetrieveUpdateDestroyAPIView):
    """
    get:
    Get a specific user by id

    Get one user by passing the user-id as a parameter into the URL.

    put:
    Update a specific user by id

    Update the entire content of a specific user. The entire data is required and will be overwritten.

    patch:
    Update parts of a specific user by id

    Update partial data of a specific user.

    delete:
    Delete a user by id

    Delete a user by passing the user id as a parameter into the URL.
    """
    permission_classes = [
        IsAuthenticated,
        IsUserOrReadOnly
    ]
    queryset = User.objects.all()
    serializer_class = UserSerializer
