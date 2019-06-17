# Generated by Django 2.0.6 on 2019-03-20 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LeaveRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Time', models.DateTimeField(auto_now=True)),
                ('Sender_mail', models.EmailField(max_length=254)),
                ('Sender', models.CharField(max_length=50)),
                ('Application', models.TextField(max_length=5000)),
            ],
        ),
    ]