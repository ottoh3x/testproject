# Generated by Django 3.0.8 on 2021-02-03 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='fullname',
            field=models.CharField(max_length=40),
        ),
    ]
