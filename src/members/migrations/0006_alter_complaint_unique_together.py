# Generated by Django 3.2.8 on 2021-11-06 19:34

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('members', '0005_alter_complaint_topic_data'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='complaint',
            unique_together={('title', 'user_name')},
        ),
    ]
