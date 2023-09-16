# Generated by Django 4.0.5 on 2022-08-29 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_tags_for_articles_alter_article_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='blog.tags_for_articles'),
        ),
    ]
