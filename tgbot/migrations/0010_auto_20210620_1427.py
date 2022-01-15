# Generated by Django 3.1.6 on 2021-06-20 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tgbot', '0009_auto_20210620_0037'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='order_number',
            field=models.CharField(db_index=True, default=1000, max_length=25, unique=True, verbose_name='Номер Заказа'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='UserAddresses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('address', models.TextField(max_length=150, verbose_name='Адрес доставки')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tgbot.tguser')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]