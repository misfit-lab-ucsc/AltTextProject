# Generated by Django 4.2.6 on 2024-05-10 21:46

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0013_post_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=-1, scale=None, size=[300, 300], upload_to='post_pics'),
        ),
    ]