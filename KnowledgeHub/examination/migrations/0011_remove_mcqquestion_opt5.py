# Generated by Django 3.2.9 on 2022-04-27 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('examination', '0010_mcqquestion_opt5'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mcqquestion',
            name='opt5',
        ),
    ]
