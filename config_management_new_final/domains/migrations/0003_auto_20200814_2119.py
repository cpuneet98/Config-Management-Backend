# Generated by Django 2.2.15 on 2020-08-14 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domains', '0002_auto_20200814_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]