from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Comment
from datetime import datetime


"""Функция отображения главной страницы"""
def index(request):
    return render(
        request,
        'index.html'
    )


class PostsList(ListView):
    model = Post
    ordering = 'post_title'

    # Имя шаблона
    template_name = 'posts.html'

    # Зависит от регистра.
    context_object_name = 'posts'

    # переопределяем метод дженерика
    # добавляем 2 переменных
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        return context

    # Использование фильтра по цене (пример)
    # queryset = Post.objects.filter(
    #     price__lt=300
    # ).order_by(
    #     'post_title'
    # )


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
    pk_url_kwarg = 'id'


class CommentsPost(ListView):
    model = Comment
    ordering = 'comment_date'
    template_name = 'post.html'
    context_object_name = 'comments'
