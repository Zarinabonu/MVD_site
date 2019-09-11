# Generated by Django 2.2.4 on 2019-09-11 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_international_busines'),
    ]

    operations = [
        migrations.RenameField(
            model_name='international_busines',
            old_name='description',
            new_name='description_ru',
        ),
        migrations.RenameField(
            model_name='international_busines',
            old_name='title',
            new_name='title_ru',
        ),
        migrations.AddField(
            model_name='international_busines',
            name='description_uz',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='international_busines',
            name='title_uz',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]