# Generated by Django 4.1.5 on 2023-11-15 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datarepo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('discription', models.TextField()),
            ],
        ),
    ]
