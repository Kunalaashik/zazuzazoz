# Generated by Django 4.0.3 on 2022-05-01 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='numbers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number1', models.IntegerField(max_length=500)),
                ('number2', models.IntegerField(max_length=500)),
                ('sum', models.IntegerField(max_length=500)),
            ],
        ),
    ]
