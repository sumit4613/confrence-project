# Generated by Django 2.1.1 on 2018-09-12 16:51

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0003_auto_20180912_2218'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Submissions',
            new_name='Submission',
        ),
    ]
