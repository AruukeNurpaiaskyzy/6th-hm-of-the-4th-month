# Generated by Django 5.1 on 2024-08-24 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_main_image_making_alter_main_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Forms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titleimg', models.CharField(max_length=255)),
            ],
        ),
    ]