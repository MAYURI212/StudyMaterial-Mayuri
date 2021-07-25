# Generated by Django 3.2.5 on 2021-07-21 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudyMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True)),
                ('content_type', models.CharField(max_length=50, null=True)),
                ('upload', models.FileField(null=True, upload_to='uploads')),
                ('subject', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
