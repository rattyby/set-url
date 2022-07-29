from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, ArticleTag, Tag


class ArticleTagInlineFormSet(BaseInlineFormSet):
    def clean(self):
        main_tags = 0
        tags = []
        for form in self.forms:
            main_tags += form.cleaned_data['is_main']
            if form.cleaned_data['tag'] not in tags:
                tags.append(form.cleaned_data['tag'])
            else:
                raise ValidationError('Разделы не должны повторяться.')
        if main_tags != 1:
            raise ValidationError('У статьи должен быть ровно один главный раздел!')
        return super().clean()


class ArticleTagAdminInline(admin.TabularInline):
    model = ArticleTag
    formset = ArticleTagInlineFormSet
    fields = ('tag', 'is_main')
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'published_at')
    inlines = (ArticleTagAdminInline,)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = 'name',


class ArticleTagAdmin(admin.ModelAdmin):
    list_display = ('is_main',)
    fields = ('tag', 'is_main')
