# Generated by Django 3.1.6 on 2021-06-19 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tgbot', '0008_auto_20210620_0032'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderproduct',
            old_name='order_id',
            new_name='order',
        ),
        migrations.RenameField(
            model_name='orderproduct',
            old_name='product_id',
            new_name='product',
        ),
    ]
