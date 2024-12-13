# Generated by Django 5.1.4 on 2024-12-12 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_name', models.CharField(max_length=255)),
                ('version', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
    ]
