# Generated by Django 3.2.9 on 2021-11-26 23:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('examination', '0007_alter_sheduledexam_duration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memberexamresult',
            name='totalMark',
        ),
        migrations.AddField(
            model_name='memberexamresult',
            name='solution',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='sheduledexam',
            name='submittedMember',
            field=models.ManyToManyField(blank=True, related_name='Submitted_Member', to=settings.AUTH_USER_MODEL),
        ),
    ]
