# Generated by Django 3.0.8 on 2020-08-01 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20200801_1525'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='child_details',
            name='nutrition_days',
        ),
        migrations.RemoveField(
            model_name='child_details',
            name='nutrition_eligible_from',
        ),
        migrations.RemoveField(
            model_name='child_details',
            name='nutrition_eligible_till',
        ),
        migrations.RemoveField(
            model_name='pregnant_details',
            name='nutrition_days',
        ),
        migrations.RemoveField(
            model_name='pregnant_details',
            name='nutrition_eligible_from',
        ),
        migrations.RemoveField(
            model_name='pregnant_details',
            name='nutrition_eligible_till',
        ),
    ]