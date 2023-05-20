from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    path( "", BlogListView.as_view(), name="home" ),                            # Home
    path( "post/<int:pk>", BlogDetailView.as_view(), name="post_detail" ),      # Post detail
    path( "post/new/", BlogCreateView.as_view(), name="post_new"),              # Create a new post
    path( "post/<int:pk>/edit", BlogUpdateView.as_view(), name="post_edit"),    # Edit a post
    path( "post/<int:pk>/delete", BlogDeleteView.as_view(), name="post_delete"),# Delete a post
]