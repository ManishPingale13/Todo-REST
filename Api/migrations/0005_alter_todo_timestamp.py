# Generated by Django 4.1.2 on 2022-10-30 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0004_alter_todo_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='timeStamp',
            field=models.DateTimeField(default='YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]'),
        ),
    ]