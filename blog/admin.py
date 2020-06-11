from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment
# Register your models here.

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)
    list_display = ('title', 'slug', 'created_date')
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Post, PostAdmin)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    '''Admin View for Comment'''

    list_display = ('author', 'body', 'post', 'created_date')
    list_filter = ('created_date',)
    search_fields = ('author','body')