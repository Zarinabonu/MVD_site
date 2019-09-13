# Generated by Django 2.2.4 on 2019-09-13 04:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Criminal_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(blank=True, max_length=100, null=True)),
                ('name_ru', models.CharField(blank=True, max_length=100, null=True)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='media')),
                ('count', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'criminal_type',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ru', models.CharField(blank=True, max_length=100, null=True)),
                ('name_uz', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'menu',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(blank=True, max_length=100, null=True)),
                ('name_ru', models.CharField(blank=True, max_length=100, null=True)),
                ('count', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'region',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ru', models.CharField(blank=True, max_length=100, null=True)),
                ('name_uz', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'type',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Type_form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ru', models.CharField(blank=True, max_length=100, null=True)),
                ('name_uz', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'type_form',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Type_news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ru', models.CharField(blank=True, max_length=100, null=True)),
                ('name_uz', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'type_news',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Submenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(blank=True, max_length=100, null=True)),
                ('name_ru', models.CharField(blank=True, max_length=100, null=True)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Menu')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Type')),
            ],
            options={
                'db_table': 'submenu',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_name_uz', models.CharField(blank=True, max_length=255, null=True)),
                ('title_name_ru', models.CharField(blank=True, max_length=255, null=True)),
                ('description_name_uz', models.TextField(blank=True, null=True)),
                ('description_name_ru', models.TextField(blank=True, null=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Type_news')),
            ],
        ),
        migrations.CreateModel(
            name='International_busines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_ru', models.CharField(blank=True, max_length=100, null=True)),
                ('title_uz', models.CharField(blank=True, max_length=100, null=True)),
                ('description_ru', models.TextField(blank=True, null=True)),
                ('description_uz', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('views', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Forms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_name_uz', models.CharField(blank=True, max_length=255, null=True)),
                ('title_name_ru', models.CharField(blank=True, max_length=255, null=True)),
                ('description_name_uz', models.TextField(blank=True, null=True)),
                ('description_name_ru', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('created', models.DateField(auto_now_add=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Type_form')),
            ],
        ),
        migrations.CreateModel(
            name='Criminal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description_name_uz', models.TextField(blank=True, null=True)),
                ('description_name_ru', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('created', models.DateField(auto_now_add=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Criminal_type')),
            ],
        ),
    ]
