# Generated by Django 3.0.8 on 2020-07-25 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Child_details',
            fields=[
                ('c_id', models.AutoField(primary_key=True, serialize=False)),
                ('c_fname', models.CharField(max_length=200)),
                ('c_lname', models.CharField(max_length=200)),
                ('c_mname', models.CharField(max_length=200)),
                ('c_gender', models.CharField(max_length=200)),
                ('c_dob', models.DateField()),
                ('c_blood_group', models.CharField(max_length=50)),
                ('c_height', models.CharField(max_length=100)),
                ('c_weight', models.CharField(max_length=100)),
                ('c_catagory', models.CharField(max_length=200)),
                ('c_email_id', models.EmailField(blank=True, max_length=100, null=True, unique=True)),
                ('c_mobile_num', models.CharField(max_length=10, unique=True)),
                ('c_address', models.CharField(max_length=200)),
                ('c_pincode', models.CharField(max_length=6)),
                ('state', models.CharField(default='Null', max_length=50)),
                ('city', models.CharField(default='Null', max_length=50)),
                ('c_adhar_number', models.CharField(max_length=12)),
            ],
            options={
                'db_table': 'child_details',
            },
        ),
    ]
