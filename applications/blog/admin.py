from django.contrib import admin
from .models import Post, Category


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title', ]
    list_display = ['title', ]


class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'content']
    list_display = ['title', 'category']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
