# Generated by Django 3.2.3 on 2021-06-07 20:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('net', '0007_auto_20210606_1801'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('subject', models.CharField(max_length=100)),
                ('is_read', models.BooleanField(default=False)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
            },
        ),
    ]
