from django import template
from django.templatetags.static import static

register = template.Library()

@register.simple_tag
def image_or_default(photo):
    print("photo", photo)
    try:
        return photo.url
    except Exception:
        return static('img/noPhoto.jpg')
