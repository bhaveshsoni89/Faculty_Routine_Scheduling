# Generated by Django 2.0.6 on 2019-03-26 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Daily_activity', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyactivity',
            name='Date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='dailyactivity',
            name='faculty',
            field=models.CharField(default='Example User', max_length=50),
            preserve_default=False,
        ),
    ]
