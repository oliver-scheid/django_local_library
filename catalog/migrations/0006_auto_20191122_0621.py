# Generated by Django 2.2.6 on 2019-11-22 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20191122_0611'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['last_name', 'first_name'], 'permissions': (('can_create_author', 'Can create a new Author'), ('can_delete_author', 'Can delete an Author'), ('can_edit_author', 'Can edit an Author'))},
        ),
    ]