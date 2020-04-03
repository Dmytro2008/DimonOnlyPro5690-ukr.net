from django.contrib import admin

from mediaportalapp.models import Category, Article


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
# Register your models here.
