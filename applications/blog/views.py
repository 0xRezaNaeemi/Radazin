from .models import Post
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class PostListView(ListView):
    model = Post
    template_name = 'blog/post-list.html'
    context_object_name = 'posts'
    paginate_by = 9


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post-detail.html'
    context_object_name = 'post'

# class MainBlog(TemplateView):
#     template_name = 'blog/blog.html'


# class PostList(TemplateView):

#     def get(self, request, **kwargs):

#         posts = Post.published.all().order_by('-created_at')[:9]
#         featured_posts = Post.published.filter(
#             featured=True).order_by('-created_at')[:3]
#         context = {
#             'posts': posts,
#             'featured_posts': featured_posts,
#         }

#         return render(request, 'blog/post-list.html', context)


# class PostDetail(TemplateView):

#     def get(self, request, slug):

#         posts = Post.published.all(slug=slug)
#         context = {
#             'posts': posts
#         }
#         return render(request, 'blog/post-detail.html', context)


# def post_list(request):
#     # articles = Article.objects.all()
#     # articles = Article.objects.filter(status='published')
#     posts = Post.published.all()
#     context = {
#         'posts': posts
#     }
#     return render(request, 'blog/post-list.html', context)



