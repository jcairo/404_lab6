from django.contrib import admin

# Register your models here.
from main.models import Link, Tag
admin.site.register(Link)
admin.site.register(Tag)
