from django.urls import path

from post.views import ListCreatePostView, RetrieveUpdateDestroyPostView, ListOwnPostView, ListUserPostView, ListLikedPostView, ToggleLikeView

urlpatterns = [
    path("", ListCreatePostView.as_view()),
    path("<int:id>/", RetrieveUpdateDestroyPostView.as_view()),
    path("me/", ListOwnPostView.as_view()),
    path("user/<int:userID>/", ListUserPostView.as_view()),
    path("likes/", ListLikedPostView.as_view()),
    path("toggle-like/<int:postID>/", ToggleLikeView.as_view()),
]

