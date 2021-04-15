# Generated by Django 3.2 on 2021-04-15 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='rassavni_foundation',
            fields=[
                ('rss_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=50)),
                ('img', models.ImageField(default='', upload_to='blog/images')),
                ('body', models.TextField(default='')),
                ('draft', models.BooleanField(default=True)),
                ('last', models.DateTimeField(auto_now=True)),
                ('writer', models.CharField(default='', max_length=40)),
            ],
        ),
    ]
