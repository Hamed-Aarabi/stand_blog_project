from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Profile(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    fathers_name = models.CharField(max_length=30)
    melicode = models.CharField(max_length=10, primary_key=True)
    image = models.ImageField(upload_to='profile/images', blank=True, null=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.name.username
    
    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.melicode)
        super(Profile, self).save()

    class Meta:
        verbose_name = 'حساب کاربری'
        verbose_name_plural = 'حساب های کاربری'