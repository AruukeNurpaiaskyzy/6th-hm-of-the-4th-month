# Generated by Django 5.1 on 2024-08-25 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_forms3'),
    ]

    operations = [
        migrations.CreateModel(
            name='Minilogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='minilogo', verbose_name='Фото')),
            ],
            options={
                'verbose_name_plural': 'minilogos',
            },
        ),
    ]
