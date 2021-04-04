# Generated by Django 3.1.7 on 2021-03-12 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_user_ethereum_private_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='ethereum_private_key',
        ),
        migrations.RemoveField(
            model_name='user',
            name='ethereum_public_key',
        ),
        migrations.RemoveField(
            model_name='user',
            name='institution',
        ),
        migrations.RemoveField(
            model_name='user',
            name='staff',
        ),
        migrations.AddField(
            model_name='user',
            name='access_token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
