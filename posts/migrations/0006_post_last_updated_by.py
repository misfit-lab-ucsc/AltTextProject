# Generated by Django 4.1.6 on 2023-04-13 23:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0005_alter_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='last_updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='last_updated_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
