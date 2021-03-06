# Generated by Django 2.1.4 on 2018-12-12 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_auto_20181212_0816'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['last_name', 'first_name'], 'permissions': (('can_create_author', 'Create new author'), ('can_update_author', 'Update author details'), ('can_delete_author', 'Delete author'))},
        ),
    ]
