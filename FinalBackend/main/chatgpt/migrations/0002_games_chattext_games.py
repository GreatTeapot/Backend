# Generated by Django 4.2.7 on 2023-12-16 11:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chatgpt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_name', models.CharField(max_length=50)),
                ('max_events', models.IntegerField(default=4)),
                ('story', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='chatgpt.story')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='chattext',
            name='games',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='chatgpt.games'),
        ),
    ]
