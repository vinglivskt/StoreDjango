from django.utils.http import urlencode

from goods.models import Categories
from django import template

register = template.Library()


@register.simple_tag
def tag_categories():
    return Categories.objects.all()


@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    q = context['request'].GET.dict()
    q.update(kwargs)
    return urlencode(q)
