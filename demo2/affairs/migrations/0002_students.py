# Generated by Django 4.0.1 on 2022-01-31 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('affairs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
            ],
        ),
    ]