from django.core.paginator import Paginator
from django.views.generic import TemplateView

from myFriends.models import Caretaker
from .models import Post, DogPost, LitterPost


class PostIndexView(TemplateView):
    template_name = 'myWords/index.html'
    model = Post
    posts = None
    page_size = 15
    title = None

    def get_context_data(self, **kwargs):
        self.posts = self.model.objects.all()
        page = int(kwargs['page']) if 'page' in kwargs else 1
        paginator = Paginator(self.posts, self.page_size)
        posts = paginator.page(page)
        post = self.posts.latest('posting_time') if self.posts.exists() else None
        next_page = page + 1 if posts.has_next() else None
        last_page = page - 1 if posts.has_previous() else None
        return {
            "title": "All Posts",
            "posts": posts,
            "post": post,
            "next_page": next_page,
            "last_page": last_page,
        }


class AllPostsIndexView(PostIndexView):
    title = "All Posts"


class DogPostsIndexView(PostIndexView):
    model = DogPost
    title = "Our Dogs"


class LitterPostIndexView(PostIndexView):
    model = LitterPost
    title = "Our Litters"


class CaretakerPostIndexView(PostIndexView):
    model = Caretaker
    title = "Our Caretakers"


class PostDetail(TemplateView):
    model = Post
    template_name = 'myWords/detail.html'

    def get_context_data(self, **kwargs):
        return {
            "post": self.model.objects.get(id=kwargs['id'])
        }
