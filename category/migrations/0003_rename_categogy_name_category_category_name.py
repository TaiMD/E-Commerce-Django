# Generated by Django 4.2.3 on 2023-07-28 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_alter_category_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='categogy_name',
            new_name='category_name',
        ),
    ]
