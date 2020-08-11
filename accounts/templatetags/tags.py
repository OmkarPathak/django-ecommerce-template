from django import template
import datetime

register = template.Library()

@register.filter(name='add_css')
def add_css(field, css):
    """Removes all values of arg from the given string"""
    return field.as_widget(attrs={"class": css})

@register.filter(name='get_status')
def get_status(field):
    """Removes all values of arg from the given string"""
    if field == '+':
        return 'Created'
    elif field == '~':
        return 'Modified'
    elif field == '-':
        return 'Deleted'
    else:
        return 'Unknown'

@register.filter(name='get_changed')
def get_changed(field, changed):
    for change in changed:
        if field == change.field:
            return 'changed'
    return ''

@register.filter(name='get_old_value')
def get_old_value(value, changed):
    for change in changed:
        if value == change.new:
            return '(' + str(change.old) + ')'
    return ''

@register.filter(expects_localtime=True)
def is_older(value):
    if isinstance(value, datetime.datetime):
        if value < datetime.datetime.now():
            return True
    return False