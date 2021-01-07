from django.contrib import admin

# Register your models here.

from .models import Member
from .models import Event
from .models import Group

admin.site.register(Member)
admin.site.register(Event)
admin.site.register(Group)