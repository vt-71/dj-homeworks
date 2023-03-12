from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag, Scope

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        self.count_is_main_tag = 0
        if len(self.forms) == 0:
            raise ValidationError('Не указаны теги!')        
        else:
            count = 0
            for form in self.forms:
                if form.cleaned_data['is_main']:
                    count += 1
            if count > 1:
                raise ValidationError('Основной тэг должен быть один!')
            elif count == 0:
                raise ValidationError('Не отмечен основной тэг!')
            else:
                    return super().clean()
        return super().clean()


        # for form in self.forms:
        #     if self.count_is_main_tag > 0 and form.cleaned_data.get('is_main'):
        #         raise ValidationError('Главный может быть только 1 тег')
        #     else:
        #         if form.cleaned_data.get('is_main'):
        #             print(f"{form.cleaned_data.get('tag')} - главный раздел")
        #             self.count_is_main_tag += 1
        #         else:
        #             continue

        return super().clean()
    
class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 0

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'published_at']
    list_display_links = ['id', 'title']
    inlines = [ScopeInline]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']

    



    
