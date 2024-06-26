# Generated by Django 5.0.2 on 2024-02-25 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NTT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='ntt/director')),
                ('name', models.CharField(max_length=550)),
                ('director', models.CharField(max_length=255)),
                ('register_number', models.CharField(max_length=550)),
                ('membership', models.CharField(max_length=550)),
                ('purpose', models.TextField()),
                ('direction', models.TextField()),
                ('projects', models.TextField()),
                ('address', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'NNT Tashkilotlari',
            },
        ),
    ]
