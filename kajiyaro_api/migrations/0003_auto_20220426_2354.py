# Generated by Django 3.1 on 2022-04-26 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kajiyaro_api', '0002_auto_20220426_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housework',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
