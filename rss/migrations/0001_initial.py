# Generated by Django 3.2 on 2021-04-15 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='aboutme',
            fields=[
                ('about_id', models.AutoField(primary_key=True, serialize=False)),
                ('about_Desc', models.CharField(default='', max_length=350)),
            ],
        ),
        migrations.CreateModel(
            name='cert',
            fields=[
                ('cert_id', models.AutoField(primary_key=True, serialize=False)),
                ('cert_names', models.CharField(default='', max_length=120)),
                ('cert_images', models.ImageField(default='', upload_to='rss/images')),
            ],
        ),
        migrations.CreateModel(
            name='cop',
            fields=[
                ('cop_id', models.AutoField(primary_key=True, serialize=False)),
                ('cop_name', models.CharField(default='', max_length=65)),
                ('cop_img', models.ImageField(default='', upload_to='rss/images')),
            ],
        ),
        migrations.CreateModel(
            name='ed_qua',
            fields=[
                ('ed_qua_id', models.AutoField(primary_key=True, serialize=False)),
                ('ed_qua_name', models.CharField(default='', max_length=201)),
                ('ed_qua_descr', models.CharField(default='', max_length=201)),
            ],
        ),
        migrations.CreateModel(
            name='events',
            fields=[
                ('eve_id', models.AutoField(primary_key=True, serialize=False)),
                ('eve_name', models.CharField(default='', max_length=120)),
                ('eve_desc', models.CharField(default='', max_length=620)),
                ('img', models.ImageField(default='', upload_to='rss/images')),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProfessionalExperience',
            fields=[
                ('ProfessionalExperience_id', models.AutoField(primary_key=True, serialize=False)),
                ('ProfessionalExperience_post', models.CharField(default='', max_length=120)),
                ('ProfessionalExperience_company', models.CharField(default='', max_length=120)),
                ('ProfessionalExperience_description', models.CharField(default='', max_length=350)),
            ],
        ),
        migrations.CreateModel(
            name='rassav',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rassav_name', models.CharField(max_length=50)),
                ('desc', models.CharField(default='', max_length=250)),
                ('current_position', models.CharField(default='', max_length=200)),
                ('image', models.ImageField(default='', upload_to='rss/images')),
                ('back_img', models.ImageField(default='', upload_to='rss/images')),
            ],
        ),
        migrations.CreateModel(
            name='skill',
            fields=[
                ('skill_id', models.AutoField(primary_key=True, serialize=False)),
                ('skill_name', models.CharField(default='', max_length=350)),
            ],
        ),
    ]
