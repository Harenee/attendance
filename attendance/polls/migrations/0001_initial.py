# Generated by Django 2.0.2 on 2018-04-17 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_no', models.IntegerField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('dob', models.IntegerField(max_length=20)),
                ('department', models.CharField(max_length=50)),
                ('clas', models.CharField(max_length=20)),
                ('batch', models.IntegerField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('mobie', models.CharField(max_length=10)),
            ],
        ),
    ]
