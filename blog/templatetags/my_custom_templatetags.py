from django.template import Library
from blog.models import Article

register = Library()


# Inclusion tags

@register.inclusion_tag('blog_app/includion_customtag.html')
def tag_clouds_section(queryset):
    return {'queryset':queryset}


