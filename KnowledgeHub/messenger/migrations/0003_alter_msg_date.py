# Generated by Django 3.2.9 on 2022-02-09 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0002_msg_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msg',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]