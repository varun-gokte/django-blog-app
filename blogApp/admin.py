from django.contrib import admin
from blogApp.models import Blog_Post, Blog_PostAdmin, Comments

# Register your models here.
admin.site.register(Blog_Post, Blog_PostAdmin)
admin.site.register(Comments)