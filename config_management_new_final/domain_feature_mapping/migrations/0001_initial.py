# Generated by Django 2.2.15 on 2020-08-16 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('features', '0001_initial'),
        ('domains', '0004_auto_20200814_2322'),
    ]

    operations = [
        migrations.CreateModel(
            name='DomainFeatureMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='domains.Domain')),
                ('feature_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='features.Feature')),
            ],
            options={
                'unique_together': {('domain_id', 'feature_id')},
            },
        ),
    ]