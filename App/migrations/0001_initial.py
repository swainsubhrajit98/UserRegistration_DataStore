# Generated by Django 4.1.7 on 2023-03-01 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('dob', models.DateField()),
                ('phone', models.IntegerField()),
                ('address', models.TextField()),
                ('country', models.TextField()),
                ('state', models.TextField()),
                ('zip', models.IntegerField(max_length=6)),
            ],
        ),
    ]