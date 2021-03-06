# Generated by Django 2.0.3 on 2019-08-20 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('type', models.CharField(blank=True, max_length=250, null=True)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('upadted', models.DateTimeField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, upload_to='picture')),
                ('author', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
    ]
