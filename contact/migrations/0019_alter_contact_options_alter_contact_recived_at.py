# Generated by Django 4.0.5 on 2022-09-15 13:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0018_alter_contact_recived_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'پیام', 'verbose_name_plural': 'پیام ها'},
        ),
        migrations.AlterField(
            model_name='contact',
            name='recived_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 15, 17, 58, 18, 527886)),
        ),
    ]
