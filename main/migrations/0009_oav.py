# Generated by Django 5.0.2 on 2024-05-07 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='OAV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_field', models.CharField(choices=[('TV', 'TV'), ('Gazeta', 'Gazeta'), ('Jurnal', 'Jurnal')], max_length=20)),
                ('name', models.CharField(max_length=255)),
                ('body', models.TextField()),
            ],
        ),
    ]