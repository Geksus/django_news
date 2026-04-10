from django.contrib import admin

from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "body", "author")
    list_filter = ("author", "date")
    search_fields = ("title", "body", "author__username")
    ordering = ("-date",)


admin.site.register(Article, ArticleAdmin)
