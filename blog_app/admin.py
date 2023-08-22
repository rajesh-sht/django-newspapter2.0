from django.contrib import admin

from blog_app.models import Category, Comment, NewsLetter, Post, Tag, Contact

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(NewsLetter)
admin.site.register(Comment)
admin.site.register(Contact)
