# Generated by Django 4.0.6 on 2022-07-14 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_relationship_alter_article_options_tag_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='articles',
        ),
    ]
