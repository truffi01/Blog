
from django.urls import path
from .views import HomePage, PostView, CreatePostView

urlpatterns = [
    path('', HomePage.as_view(), name= "blog-home"),
    path('post/<int:pk>/', PostView.as_view(), name="post-detail"),
    path('create_post/', CreatePostView.as_view(success_url='/'), name = "create_post")
]