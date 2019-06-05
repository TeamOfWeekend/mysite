# Generated by Django 2.1.7 on 2019-06-05 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colleges', '0004_auto_20190605_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academyinfo',
            name='academyId',
            field=models.BigIntegerField(unique=True, verbose_name='学院编号'),
        ),
        migrations.AlterField(
            model_name='majorinfo',
            name='majorId',
            field=models.BigIntegerField(unique=True, verbose_name='专业编号'),
        ),
    ]
