from django.urls import path
import blog.views as blog_views

urlpatterns = [
    path("", blog_views.post_list, name="post_list"),
    path("post_details/<int:post_id>", blog_views.post_details, name="post_details"),
    path("author_post_list/<int:author_id>", blog_views.author_post_list, name="author_post_details")
]