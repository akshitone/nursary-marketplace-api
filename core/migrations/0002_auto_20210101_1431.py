# Generated by Django 3.1.3 on 2021-01-01 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='name',
            field=models.TextField(),
        ),
    ]
