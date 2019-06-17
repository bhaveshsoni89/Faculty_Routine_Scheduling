# Generated by Django 2.0.6 on 2019-03-20 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
                ('report', models.TextField()),
                ('sender', models.CharField(blank=True, max_length=50)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]