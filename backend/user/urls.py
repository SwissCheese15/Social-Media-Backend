from django.urls import path
from .views import ListCreateUserView, RetrieveUpdateDestroyUserAPIView, ListFollowersUserView, ListPeopleTheUserFollowsView, ToggleFollowView, ListPostsOfFollowedPeopleView

urlpatterns = [
    path('users/', ListCreateUserView.as_view()),
    path("users/<int:pk>/", RetrieveUpdateDestroyUserAPIView.as_view()),
    path("social/followers/followers/", ListFollowersUserView.as_view()),
    path("social/followers/following/", ListPeopleTheUserFollowsView.as_view()),
    path("social/followers/toggle-follow/<int:userID>/", ToggleFollowView.as_view()),
    path("social/posts/following/", ListPostsOfFollowedPeopleView.as_view()),
]