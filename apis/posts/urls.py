from django.urls import path
from apis.posts import views

urlpatterns = [
    path('', views.PostView.as_view()),
    path('<int:pk>/', views.PostView.as_view()),
    path('<int:post_id>/comments/', views.CommentView.as_view())
]