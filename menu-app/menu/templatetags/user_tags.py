from django import template
from django.db.models import Value
from django.db.models.functions import Length, Replace

from ..models import Menu

register = template.Library()

OFFSET = 10


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, name):
    requested_url = context['request'].path
    subquery = Menu.objects.filter(title=name).values('url')[:1]
    menu = Menu.objects.filter(
        url__startswith=subquery).annotate(
        lvl=Length('url') - Length(
            Replace('url', Value('/'), Value(''))) + OFFSET).order_by(
        'lvl', 'position')

    local_context = {
        'menu': menu,
        'lvl': requested_url.count('/') + 1 + OFFSET
    }
    return local_context
