# Generated by Django 2.2.5 on 2019-09-26 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0004_auto_20190926_2100'),
    ]

    operations = [
        migrations.CreateModel(
            name='maintenance_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
    ]
