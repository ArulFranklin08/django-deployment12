# Generated by Django 2.2.5 on 2020-11-12 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tracking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.IntegerField(null=True)),
                ('order_id', models.IntegerField(null=True)),
                ('phone_no', models.IntegerField(null=True)),
            ],
        ),
    ]
