# Generated by Django 2.2.5 on 2019-09-06 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
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
            name='ListContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz_title', models.CharField(blank=True, max_length=100, null=True)),
                ('name_ru_title', models.CharField(blank=True, max_length=100, null=True)),
                ('name_uz_description', models.CharField(blank=True, max_length=100, null=True)),
                ('name_ru_description', models.CharField(blank=True, max_length=100, null=True)),
                ('source', models.CharField(blank=True, max_length=100, null=True)),
                ('view', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
                ('date', models.DateField(auto_now_add=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('submenu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Submenu')),
            ],
        ),
        migrations.CreateModel(
            name='DetailContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz_title', models.CharField(blank=True, max_length=100, null=True)),
                ('name_ru_title', models.CharField(blank=True, max_length=100, null=True)),
                ('name_uz_description', models.CharField(blank=True, max_length=100, null=True)),
                ('name_ru_description', models.CharField(blank=True, max_length=100, null=True)),
                ('source', models.CharField(blank=True, max_length=100, null=True)),
                ('view', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
                ('date', models.DateField(auto_now_add=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('start_date', models.DateField(blank=True, null=True)),
                ('finish_date', models.DateField(blank=True, null=True)),
                ('submenu', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.Submenu')),
            ],
        ),
    ]