# Generated by Django 2.2.4 on 2019-09-13 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20190913_1128'),
    ]

    operations = [
        migrations.RenameField(
            model_name='international_busines',
            old_name='title_ru',
            new_name='title_name_ru',
        ),
        migrations.RenameField(
            model_name='international_busines',
            old_name='title_uz',
            new_name='title_name_uz',
        ),
    ]
