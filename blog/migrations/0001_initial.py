# Generated by Django 4.0.4 on 2022-04-27 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('profession', models.CharField(max_length=299)),
                ('email', models.EmailField(max_length=254)),
                ('image', models.ImageField(upload_to='')),
                ('insta', models.URLField(blank=True, null=True)),
                ('whatsapp', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'About Us',
                'verbose_name_plural': 'About Us',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.CreateModel(
            name='Schedules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('day', models.CharField(choices=[('1', 'ПОНЕДЕЛЬНИК'), ('2', 'ВТОРНИК'), ('3', 'СРЕДА'), ('4', 'ЧЕТВЕРГ'), ('5', 'ПЯТНИЦА'), ('6', 'СУББОТА')], max_length=255)),
                ('time_begining', models.TimeField()),
                ('text', models.CharField(max_length=355)),
            ],
            options={
                'verbose_name': 'Schedules',
                'verbose_name_plural': 'Schedules',
                'ordering': ['time_begining'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=55)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=50)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=255)),
                ('class_image', models.ImageField(upload_to='')),
                ('class_price', models.IntegerField()),
                ('opisanie', models.TextField()),
                ('trainer_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.aboutus')),
            ],
            options={
                'verbose_name': 'Class',
                'verbose_name_plural': 'Classes',
            },
        ),
    ]