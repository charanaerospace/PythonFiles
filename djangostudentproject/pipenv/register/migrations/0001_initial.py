# Generated by Django 4.0.6 on 2022-07-13 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=10)),
                ('department', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=10)),
                ('mobile', models.IntegerField(max_length=10)),
                ('semester', models.IntegerField(max_length=10)),
            ],
        ),
    ]
