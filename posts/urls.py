
from django.urls import path
from .views import HomePage, PostView

urlpatterns = [
    path('', HomePage.as_view(), name= "blog-home"),
    path('post/<int:pk>/', PostView.as_view(), name='post_detail')
]