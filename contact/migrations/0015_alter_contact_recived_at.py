# Generated by Django 4.0.5 on 2022-09-13 13:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0014_alter_contact_recived_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='recived_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 13, 13, 30, 40, 66107, tzinfo=utc)),
        ),
    ]
