# Generated by Django 2.0.3 on 2019-09-14 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, default='abc', null=True, unique=True),
        ),
    ]
