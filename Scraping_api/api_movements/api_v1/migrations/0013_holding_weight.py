# Generated by Django 4.1.4 on 2024-01-30 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v1', '0012_rename_balance_balance_balance_ars_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='holding',
            name='weight',
            field=models.FloatField(default=0),
        ),
    ]
