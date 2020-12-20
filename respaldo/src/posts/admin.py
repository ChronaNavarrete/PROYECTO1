from django.contrib import admin
from .models import Post, PostView, Like, Comment, User, Profile, Dislike
# Register your models here.

admin.site.register(Post)
admin.site.register(PostView)
admin.site.register(Like)
admin.site.register(Dislike)
admin.site.register(Comment)
admin.site.register(User)
admin.site.register(Profile)