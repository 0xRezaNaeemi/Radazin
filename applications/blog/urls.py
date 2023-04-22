from django.urls import path
from . import views


app_name = "blog"
urlpatterns = [
    # path('', views.MainBlog.as_view, name='main_blog'),
    path('', views.PostListView.as_view(), name='post_list'),
    path('<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
]

