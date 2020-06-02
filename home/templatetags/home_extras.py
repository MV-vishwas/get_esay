from django import template
register=template.Library()
def change_row(value):
    if value%3==0:
        return True
    else:
        return False
register.filter('change_row',change_row)