from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 
from .forms import EmailPostForm, CommentForm, SearchForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.postgres.search import TrigramSimilarity
from taggit.models import Tag 
from django.views.decorators.http import require_POST
from django.db.models import Count

def redirect_posts(request):
    return HttpResponseRedirect('/blog/')


def post_search(request):
    form = SearchForm()
    query = None
    results = []

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']

            results = Post.published.annotate(similarity=TrigramSimilarity('title', query)).filter(similarity__gt=0.1).order_by('-similarity')

    return render(request, 'blog/post/search.html', {'form': form, 'query': query, 'results': results})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                            status=Post.Status.PUBLISHED,
                            slug=post,
                            publish__year=year,
                            publish__month=month,
                            publish__day=day,)

    comments = post.comments.filter(active=True)

    form = CommentForm()

    post_tags_ids = post.tags.values_list('id', flat=True)

    similar_post = Post.published.filter(tags__in=post_tags_ids) \
        .exclude(id=post.id)

    similar_posts = similar_post.annotate(same_tags=Count('tags')) \
        .order_by('-same_tags', '-publish')[:4]

    return render(request, "blog/post/detail.html",
                  {"post": post,
                   'comments': comments,
                   'form': form,
                   'similar_posts': similar_posts})



def post_share(request, post_id):
    """Функция что будет совершать редирект на чью-то почту"""
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)

    sent = False

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f'{cd['name']} recomendeds you read ' \
                       f'{post.title}'
            message = f'Read {post.title} at {post_url}\n\n' \
                      f"{cd['name']}\'s ({cd['email']}) comments: {cd['comments']}"
            send_mail(subject, message, settings.EMAIL_HOST_USER, [cd['to']])  
            send_mail(subject, message, settings.EMAIL_HOST_USER, [cd['to']])          
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post,
                                                    'form': form,
                                                    'sent': sent})


@require_POST
def post_comment(request, post_id):
    """Функция что обрабатывает коментарии"""
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)

    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        form = EmailPostForm()
    return render(request, 'blog/post/comment.html', {'post': post,
                                                    'form': form,
                                                    'comment': comment})
def post_list(request, tag_slug=None):
    post_list = Post.published.all().order_by('-publish')

    tag = None
    if tag_slug: 
        tag = get_object_or_404(Tag, slug=tag_slug)
        post_list = post_list.filter(tags__in=[tag])

    paginator = Paginator(post_list, 4)

    page_number = request.GET.get('page', 1)

    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html', {'posts': posts, 'tag': tag})



def test(request):
    return render(request, 'blog/post/test.html')
