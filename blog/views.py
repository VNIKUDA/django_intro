from django.shortcuts import render
from .models import Post, Author

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    context = {
        "post_list": posts
    }

    return render(request, "blog/post_list.html", context=context)

def post_details(request, post_id):
    post = Post.objects.get(id=post_id)

    context = {
        "post": post
    }

    return render(request, "blog/post_details.html", context=context)

def author_post_list(request, author_id):
    author = Author.objects.get(id=author_id)
    posts = Post.objects.filter(author_id=author_id)

    context = {
        "author": author,
        "post_list": posts
    }

    return render(request, "blog/author_post_list.html", context=context)