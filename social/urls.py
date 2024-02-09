from django.urls import path
from .views import PostDeleteView, PostDetailView, PostEditView, AddLike, AddDislike, CommentDeleteView, CommentEditView, CommentReplyView, AddCommentDislike, AddCommentLike


app_name="social"

urlpatterns = [
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('post/edit/<int:pk>/', PostEditView.as_view(), name="post-edit"),
    path('post/delete/<int:pk>', PostDeleteView.as_view(), name="post-delete"),
    
    path('post/delete/<int:pk>/like', AddLike.as_view(), name="like"),
    path('post/delete/<int:pk>/dislike', AddDislike.as_view(), name="dislike"),
    
    path('post/<int:post_pk>/comment/delete/<int:pk>/', CommentDeleteView.as_view(), name="comment-delete"),
    path('post/<int:post_pk>/comment/edit/<int:pk>/', CommentEditView.as_view(), name="comment-edit"),

    path('post/<int:post_pk>/comment/<int:pk>/like', AddCommentLike.as_view(), name="comment-like"),
    path('post/<int:post_pk>/comment/<int:pk>/dislike', AddCommentDislike.as_view(), name="comment-dislike"),
    path('post/<int:post_pk>/comment/<int:pk>/reply',CommentReplyView.as_view(), name='comment-reply'),
]