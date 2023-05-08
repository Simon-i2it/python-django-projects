from django.contrib import admin

from post.models import Author, Post, Tag


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "date")
    list_filter = ("author", "date", "tags")
    prepopulated_fields = {"slug": ("title",)}


# Register your models here.
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
