# Generated by Django 4.1.6 on 2023-04-17 02:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_alter_post_options_alter_post_last_updated_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='altText',
            new_name='alt_text',
        ),
    ]