from django import template
register = template.Library()

@register.filter
def myslice(value, arg):
    """
    Return a slice of the list using the same syntax as Python's list slicing.
    """
    try:
        bits = []
        for x in str(arg).split(':'):
            if not x:
                bits.append(None)
            else:
                bits.append(int(x))
        return value[slice(*bits)]

    except (ValueError, TypeError):
        return value  # Fail silently.