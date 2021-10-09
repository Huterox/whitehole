# Generated by Django 3.2.6 on 2021-10-05 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0005_alter_bolg_date'),
        ('Channel', '0004_auto_20211005_1610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='channel',
            name='channel_blog',
        ),
        migrations.AddField(
            model_name='channel',
            name='channel_blog',
            field=models.ManyToManyField(null=True, to='Blog.Bolg'),
        ),
    ]