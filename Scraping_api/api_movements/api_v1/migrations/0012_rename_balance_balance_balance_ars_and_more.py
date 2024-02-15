# Generated by Django 4.1.4 on 2024-01-29 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v1', '0011_balance_last_updated'),
    ]

    operations = [
        migrations.RenameField(
            model_name='balance',
            old_name='balance',
            new_name='balance_ars',
        ),
        migrations.AddField(
            model_name='balance',
            name='balance_usd',
            field=models.DecimalField(decimal_places=2, default=4000, max_digits=10),
            preserve_default=False,
        ),
    ]
