# Generated by Django 3.2.9 on 2021-11-25 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('examination', '0002_remove_quessetdetail_passingmark'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quessetdetail',
            name='password',
        ),
    ]
