from django.urls import path
from .views import PostListView, PostDetailView,PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, CommentDeleteView
from . import views

urlpatterns = [
    path('',PostListView.as_view(), name='app-home'),
    path('user/<str:email>',UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/',PostDetailView.as_view(), name='post-detail'),
    path('post/new/',PostCreateView.as_view(), name='post-create'),
    path('about',views.about,name='app-about'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comment/',views.CommentCreateView.as_view(), name='create-comment'),
    path('post/<int:pk>/comment/delete',CommentDeleteView.as_view(), name='comment-delete'),
    path('postlike/<int:pk>/', views.PostLike, name="post-like"),
]