# Generated by Django 4.0.5 on 2022-09-13 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_article_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='pub',
            field=models.DateField(null=True),
        ),
    ]
