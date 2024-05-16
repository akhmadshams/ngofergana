# Generated by Django 5.0.2 on 2024-02-27 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_blog_grant'),
    ]

    operations = [
        migrations.CreateModel(
            name='NormativHujjat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=255)),
                ('title', models.TextField()),
                ('link', models.CharField(max_length=550)),
                ('year', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Normativ Hujjatlar',
            },
        ),
    ]
