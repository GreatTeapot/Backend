# Generated by Django 4.2.7 on 2023-12-21 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatgpt', '0002_games_chattext_games'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chattext',
            name='story',
        ),
        migrations.RemoveField(
            model_name='chattext',
            name='user',
        ),
        migrations.RemoveField(
            model_name='games',
            name='max_events',
        ),
        migrations.AddField(
            model_name='games',
            name='health',
            field=models.IntegerField(default=100),
        ),
    ]
