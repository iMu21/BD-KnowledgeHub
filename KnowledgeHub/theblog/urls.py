from django.urls import path
from .views import CommentView,LikeHomeView,HomeView,ArticleDetailView,AddPostView,AddPostView1,UpdatePostView,DeletePostView,notAllowedView,LikeView

urlpatterns = [
 path('',HomeView.as_view(),name='home'),
 path('article/<int:pk>',ArticleDetailView.as_view(),name='article-detail'),
 path('add_post/',AddPostView.as_view(),name='add_post'),
 path('add_post/AddPostView1',AddPostView1,name='add_post1'),
 path('article/edit/<int:pk>',UpdatePostView.as_view(),name='update_post'),
 path('article/delete/<int:pk>',DeletePostView.as_view(),name='delete_post'),
 path('notAllowed/',notAllowedView,name='notAllowed'),
 path('like/<int:pk>',LikeView,name="like"),
 path('comment/<int:pk>',CommentView,name="comment"),
 path('likeHome/<int:pk>',LikeHomeView,name="likeHome"),

]
