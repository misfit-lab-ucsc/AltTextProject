# Generated by Django 4.1.6 on 2023-03-13 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='altText',
            field=models.TextField(default='missing alt text', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=10),
        ),
    ]
