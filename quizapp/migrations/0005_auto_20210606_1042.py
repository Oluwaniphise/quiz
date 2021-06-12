# Generated by Django 3.2.3 on 2021-06-06 09:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quizapp', '0004_choice_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='score',
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizapp.choice')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizapp.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]