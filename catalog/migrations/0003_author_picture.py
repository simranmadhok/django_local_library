# Generated by Django 2.1.4 on 2018-12-07 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_book_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='author_images/%Y/%m/%d/'),
        ),
    ]
