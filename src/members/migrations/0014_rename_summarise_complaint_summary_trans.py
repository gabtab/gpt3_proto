# Generated by Django 3.2.9 on 2021-11-17 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0013_complaint_summarise'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complaint',
            old_name='summarise',
            new_name='summary_trans',
        ),
    ]
