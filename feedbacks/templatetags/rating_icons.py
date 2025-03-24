from django import template

register = template.Library()

@register.filter
def rating_to_icon(value):
    icons = {
        1: "fa-face-angry",
        2: "fa-face-frown",
        3: "fa-face-meh",
        4: "fa-face-smile-beam",
        5: "fa-face-grin-wink",
    }
    return icons.get(value, "fa-question-circle")
