from django.db import models



class ArticleManager(models.Manager):

    def save(self):
        print(f'{self.title} Hello.')
        super(ArticleManager, self).save()


    def counter(self):
        return len(self.all())


