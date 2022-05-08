# Generated by Django 3.2.9 on 2022-05-08 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Qrcode_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('childname', models.CharField(max_length=30)),
                ('parentname', models.CharField(max_length=30)),
                ('relationship', models.CharField(max_length=30)),
                ('streetaddress', models.CharField(max_length=30)),
                ('towncity', models.CharField(max_length=30)),
                ('postcode', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
