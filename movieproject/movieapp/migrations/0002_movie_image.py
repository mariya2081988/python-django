# Generated by Django 4.2.1 on 2023-06-15 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(default='asdf', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
