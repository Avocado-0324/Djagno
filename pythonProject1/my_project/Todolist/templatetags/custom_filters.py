# my_app/templatetags/custom_filters.py

from django import template
from django.utils import timezone

register = template.Library()

@register.filter
def days_until(due_date):
    if due_date:
        now = timezone.now()
        if timezone.is_naive(due_date):
            due_date = timezone.make_aware(due_date, timezone.get_current_timezone())
        delta = due_date - now
        return delta.days
    return ''
