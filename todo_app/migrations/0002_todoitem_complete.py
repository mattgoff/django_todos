# Generated by Django 4.0.3 on 2022-03-09 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]
