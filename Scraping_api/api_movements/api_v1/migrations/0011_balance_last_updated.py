# Generated by Django 4.1.4 on 2023-06-22 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v1', '0010_rename_logo_url_company_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='balance',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]