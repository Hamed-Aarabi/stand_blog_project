# Generated by Django 4.0.5 on 2022-07-20 12:56

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0006_rename_user_profile_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='Karbar',
        ),
    ]
