# Generated by Django 4.0.5 on 2022-09-15 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_remove_article_pub'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('-created',), 'verbose_name': 'مقاله', 'verbose_name_plural': 'مقالات'},
        ),
        migrations.AlterModelOptions(
            name='categorie',
            options={'verbose_name': 'دسته بندی', 'verbose_name_plural': 'دسته بندی ها'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-created',), 'verbose_name': 'کامنت', 'verbose_name_plural': 'کامنت ها'},
        ),
        migrations.AlterModelOptions(
            name='tags_for_articles',
            options={'verbose_name': 'تگ', 'verbose_name_plural': 'تگ ها'},
        ),
        migrations.AlterField(
            model_name='categorie',
            name='name',
            field=models.CharField(max_length=50, verbose_name='نام دسته بندی'),
        ),
        migrations.AlterField(
            model_name='tags_for_articles',
            name='tag_name',
            field=models.CharField(max_length=20, verbose_name='نام تگ'),
        ),
    ]
