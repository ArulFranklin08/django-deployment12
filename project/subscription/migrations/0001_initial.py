# Generated by Django 2.2.5 on 2020-11-12 05:32

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.IntegerField(null=True)),
                ('customer_name', models.CharField(max_length=30, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None)),
                ('plan_subscription', models.CharField(choices=[('Gold', 'Gold'), ('Silver', 'Silver'), ('Bronze', 'Bronze')], max_length=100, null=True)),
                ('payment', models.CharField(max_length=100, null=True)),
                ('Address', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription_payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.IntegerField(null=True)),
                ('Customer_name', models.CharField(max_length=100)),
                ('order_id', models.IntegerField(null=True)),
                ('trans_id', models.IntegerField(null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('email', models.CharField(max_length=100)),
                ('total_amount', models.IntegerField(null=True)),
                ('Status', models.CharField(choices=[('Active', 'Active'), ('InActive', 'InActive')], max_length=100, null=True)),
            ],
        ),
    ]
