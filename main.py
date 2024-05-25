import os, time
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MyBlog.settings")
django.setup()

from blog.models import Post, Author

# author = Author(
#     name="sanya",
#     bio=""
# )
# author.save()

# new_post = Post(
#     title="alda",
#     content="",
#     author=author
# )
# new_post.save()

post = Post(
    title="alda",
    content="",
    author=Author.objects.get(id=1),
    published_date = "2023-05-25 09:34:16.120498"
)

# time.sleep(5)
print(post.published_recently())