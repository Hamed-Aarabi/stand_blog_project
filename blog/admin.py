from django.contrib import admin
from .models import Article, Categorie, Comment, Tags_For_Articles
from django.contrib.auth.models import User

class FilterBypublish(admin.SimpleListFilter):
    title = 'وضعیت چاپ'
    parameter_name = 'published'
    def lookups(self, request, model_admin):
        return (
            ('True', 'چاپ شده'),
            ('False','چاپ نشده')
        )
    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(status=self.value())

class FilterByCategorie(admin.SimpleListFilter):
    title = 'دسته بندی'
    parameter_name = 'categorie'
    def lookups(self, request, model_admin):
        return (
            ('Movie','فیلم'),
            ('Programming','برنامه نویسی'),
            ('Django','جنگو'),
            ('Python','پایتون'),
        )

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(categorie__name=self.value())

class FilterByTags(admin.SimpleListFilter):
    title = 'تگ'
    parameter_name = 'tag'
    def lookups(self, request, model_admin):
        return (
            ('movie','فیلم'),
            ('vision','دیدگاه'),
            ('python','پایتون'),
            ('django','جنگو'),

        )
    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(tags__tag_name=self.value())


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','author', 'status', 'show_image', 'like_counter', 'dislike_counter', 'viewers_counter')
    list_editable = ('status','author')
    list_filter = (FilterBypublish,'author',FilterByCategorie,FilterByTags)
    search_fields = ('title',)
    search_help_text = 'جستوجو در عنوان مقالات'

@admin.register(Comment)
class commnetAdmin(admin.ModelAdmin):
    list_display = ('user', 'article', 'body', 'parent')
    list_filter = ('user', 'article', 'created')
    list_editable = ('body',)

admin.site.register(Categorie)
admin.site.register(Tags_For_Articles)
