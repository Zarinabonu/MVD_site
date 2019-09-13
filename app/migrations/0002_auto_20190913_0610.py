# Generated by Django 2.2.4 on 2019-09-13 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='criminal',
            old_name='description_name_ru',
            new_name='full_content_ru',
        ),
        migrations.RenameField(
            model_name='criminal',
            old_name='description_name_uz',
            new_name='full_content_uz',
        ),
        migrations.RenameField(
            model_name='forms',
            old_name='description_name_ru',
            new_name='full_content_ru',
        ),
        migrations.RenameField(
            model_name='forms',
            old_name='description_name_uz',
            new_name='full_content_uz',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='description_name_ru',
            new_name='full_content_ru',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='description_name_uz',
            new_name='full_content_uz',
        ),
        migrations.AddField(
            model_name='criminal',
            name='short_content_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='criminal',
            name='short_content_uz',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='forms',
            name='short_content_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='forms',
            name='short_content_uz',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='short_content_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='short_content_uz',
            field=models.TextField(blank=True, null=True),
        ),
    ]
