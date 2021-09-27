# Generated by Django 2.2.5 on 2019-09-26 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0003_auto_20190926_1620'),
    ]

    operations = [
        migrations.DeleteModel(
            name='user',
        ),
        migrations.RemoveField(
            model_name='council_member',
            name='muser_id',
        ),
        migrations.AddField(
            model_name='council_member',
            name='m_id',
            field=models.CharField(default='1234', max_length=25),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='council_member',
            name='department',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='council_member',
            name='password',
            field=models.CharField(max_length=40),
        ),
    ]
