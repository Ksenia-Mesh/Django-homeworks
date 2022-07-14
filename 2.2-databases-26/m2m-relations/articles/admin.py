
from django.contrib import admin

from .models import Article, Tag, Relationship
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        counter = 0
        for form in self.forms:
            for key, value in form.cleaned_data.items():
                if key == 'is_main' and value is True:
                    counter += 1
        if counter > 1:
            raise ValidationError('Основной раздел может быть только один.')

        return super().clean()


class RelationshipInline(admin.TabularInline):
    model = Relationship
    formset = RelationshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'published_at', 'image']
    list_filter = ['title']
    inlines = [RelationshipInline]



@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]