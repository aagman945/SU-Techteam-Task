# Generated by Django 3.1.7 on 2021-04-02 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traveller', '0004_auto_20210402_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='Email',
            field=models.CharField(max_length=122, null=True),
        ),
    ]