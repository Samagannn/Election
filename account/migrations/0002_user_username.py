# Generated by Django 5.1 on 2024-09-10 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default=1, max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
