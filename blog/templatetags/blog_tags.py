from django import template
from ..models import Post
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown

register = template.Library()


@register.simple_tag
def total_posts():
    return Post.published.count()



@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}
# В приведенном выше исходном коде мы зарегистрировали шаблонный тег, применяя декоратор @register.inclusion_tag.
# Используя blog/post/latest_posts.html, был указан шаблон, который будет прорисовываться возвращенными значениями.

@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(total_comments=Count('comments')).exclude(total_comments=0).order_by(
        '-total_comments')[:count]

# @register.simple_tag
# def get_most_comments_post(count=5):
#     return Post.published.annotate(
#         # Каждому объекту будет добавлена аннотация(как дополнительное поле с именем total_comments) с количеством комментариев у данного объекта, которую можно использовать далее в запросах.
#         total_comments=Count('comments')
#     ).exclude(total_comments=0).order_by('-total_comments')[:count] # Далее мы исключаем посты без комментариев, у которых total_comments=0
#     # Затем мы сортируем посты по полю аннотации, в обратном порядке
#     # И затем ограничиваем количество получаемых постов
#     # А декоратор @register.simple_tag используется чтобы зарегистрировать эту функцию в качестве шаблонного тега.


@register.filter(name='markdown')# Во избежание конфликта имен между именем функции и модулем markdown мы дали функции имя markdown_format, а фильтру – имя markdown для использования в шаблонах, в частности {{ variable|markdown }}.
def mardown_format(text):
    return mark_safe(markdown.markdown(text))
    # Мы используем предоставляемую веб-фреймворком Django функцию mark_safe, 
    # чтобы помечать результат как безопасный для прорисовки в шаблоне исходный код HTML. По умолчанию Django не будет доверять никакому исходному коду HTML и будет экранировать его перед его вставкой в результат.