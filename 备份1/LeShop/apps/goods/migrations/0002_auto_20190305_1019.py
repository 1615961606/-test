# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-05 10:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='shop_price',
            field=models.FloatField(default=0, help_text='本店价格', verbose_name='本店价格'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='sold_num',
            field=models.IntegerField(default=0, help_text='商品销售量', verbose_name='商品销售量'),
        ),
        migrations.AlterField(
            model_name='goodscategory',
            name='is_tab',
            field=models.BooleanField(default=False, help_text='是否在首页导航栏显示', verbose_name='是否导航'),
        ),
    ]
