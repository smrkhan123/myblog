from django.contrib import admin
from .models import post,like,comment
# Register your models here.
admin.site.register(post)
admin.site.register(like)
admin.site.register(comment)