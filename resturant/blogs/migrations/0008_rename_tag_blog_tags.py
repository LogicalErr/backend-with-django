# Generated by Django 4.0 on 2022-01-24 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0007_tag_blog_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='tag',
            new_name='tags',
        ),
    ]
