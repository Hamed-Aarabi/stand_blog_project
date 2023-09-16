from django import template
import datetime
import pytz
from termcolor import colored

register = template.Library()

# templates filter
@register.filter
def rials_style(value):
    return value[:3]+','+value[3:]




@register.filter
def show_body(value):
    return value[:30]+'...'




@register.filter
def replace(value, arg):
    return value.replace(' ', arg)


# template simple tags

@register.simple_tag
def current_time(format_str):
    return datetime.datetime.now().strftime(format_str)


@register.simple_tag
def tag_with_context(format_string):
   return datetime.datetime.now(pytz.timezone(format_string))