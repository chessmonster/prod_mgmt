# Generated by Django 2.2.2 on 2019-06-21 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20190621_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='display_name',
            field=models.CharField(default='test', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='sku',
            field=models.CharField(default='123123345sdfsd345435sdgf', max_length=255),
            preserve_default=False,
        ),
    ]
