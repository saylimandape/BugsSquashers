# Generated by Django 3.0.8 on 2020-07-30 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20200725_2134'),
    ]

    operations = [
        migrations.CreateModel(
            name='NGO_details',
            fields=[
                ('ngo_id', models.AutoField(primary_key=True, serialize=False)),
                ('ngo_name', models.CharField(max_length=200)),
                ('ngo_email_id', models.EmailField(blank=True, max_length=100, null=True, unique=True)),
                ('ngo_mobile_num', models.CharField(max_length=10, unique=True)),
                ('p_address', models.CharField(max_length=500)),
                ('p_pincode', models.IntegerField(max_length=6)),
                ('state', models.CharField(default='Null', max_length=50)),
                ('city', models.CharField(default='Null', max_length=50)),
                ('ngo_reg_date', models.DateTimeField(auto_now=True)),
                ('ngo_how_many_children', models.CharField(max_length=200, null=True)),
                ('ngo_file', models.FileField(upload_to='')),
            ],
            options={
                'db_table': 'NGO_details',
            },
        ),
    ]