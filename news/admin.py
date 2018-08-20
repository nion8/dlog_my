from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from news.models import News, Category, Tag, Comments


class NewsAdmin(SummernoteModelAdmin):
    summernote_fields = ('text_min', 'text')


# Register your models here.
admin.site.register(News, NewsAdmin)
admin.site.register(Category)
admin.site.register(Tag)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'new', 'created', 'moderation')


admin.site.register(Comments, CommentAdmin)
