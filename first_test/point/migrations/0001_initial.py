# Generated by Django 4.0.4 on 2022-05-09 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('url', models.CharField(max_length=1000)),
                ('keywords', models.TextField()),
            ],
        ),
    ]