# Generated by Django 5.1 on 2024-08-25 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_forms2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Forms3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='forms3', verbose_name='Фото')),
            ],
            options={
                'verbose_name_plural': 'Формы3',
            },
        ),
    ]
