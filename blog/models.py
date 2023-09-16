from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.utils.text import slugify
from . import managers
from django.urls import reverse


class Tags_For_Articles(models.Model):
    tag_name = models.CharField(max_length=20, verbose_name='نام تگ')

    def __str__(self):
        return self.tag_name

    class Meta:
        verbose_name = 'تگ'
        verbose_name_plural = 'تگ ها'


class Categorie(models.Model):
    name = models.CharField(max_length=50, verbose_name='نام دسته بندی')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class Article(models.Model):
    image = models.ImageField(upload_to='images/article', verbose_name='عکس')
    categorie = models.ManyToManyField(Categorie, related_name='articles', verbose_name='دسته بندی')
    title = models.CharField(max_length=100, help_text='یک عنوان مناسب برای مقاله انتخاب شود.', verbose_name='عنوان')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='user_art',
                               verbose_name='نویسنده')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated = models.DateTimeField(auto_now=True, verbose_name='تاریخ آخرین آپدیت')
    body = models.TextField(verbose_name='متن')
    tags = models.ManyToManyField(Tags_For_Articles, related_name='tag', null=True, verbose_name='تگ ها')
    viewers = models.ManyToManyField(User,related_name='article_viewers',editable=False, verbose_name='تعداد بازدید')
    status = models.BooleanField(default=True, verbose_name='وضعیت')
    slug = models.SlugField(unique=True, null=True, blank=True, verbose_name='اسلاگ')
    like = models.ManyToManyField(User, related_name='article_likes', verbose_name='لایک')
    dislike = models.ManyToManyField(User, related_name='article_dislikes', verbose_name='دیس لایک')

    def like_counter(self):
        return self.like.count()

    like_counter.short_description = 'نعداد لایک'

    def dislike_counter(self):
        return self.dislike.count()

    dislike_counter.short_description = 'نعداد دیس لایک'
    def viewers_counter(self):
        return self.viewers.count()

    viewers_counter.short_description = 'نعداد بازدید'

    class Meta:
        ordering = ('-created',)
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.title)
        super(Article, self).save()

    def get_absolute_url(self):
        return reverse('blog:blog_datail', kwargs={'slug': self.slug})

    def __str__(self):
        return f'{self.title} -- {self.body[:30]}'

    def show_image(self):
        return format_html(f'<img src="{self.image.url}" width="85px" height="85px">')

    show_image.short_description = 'تصویر مقاله'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', verbose_name='مقاله')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name='کاربر')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    body = models.TextField(verbose_name='پیام')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies', null=True, blank=True,
                               verbose_name='جواب به')

    class Meta:
        ordering = ('-created',)
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها'

    def __str__(self):
        return f'{self.user} -- {self.body[:20]}'
