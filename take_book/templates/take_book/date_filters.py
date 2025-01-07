from django import template
from datetime import datetime
from dateutil.relativedelta import relativedelta

register = template.Library()

@register.filter
def add_months(date, months):
    return date + relativedelta(months=months)