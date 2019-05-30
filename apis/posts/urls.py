from django.urls import path
from apis.posts import views

urlpatterns = [
    path('', views.PostView.as_view())
]