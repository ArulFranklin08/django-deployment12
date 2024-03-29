# Generated by Django 2.2.5 on 2020-11-12 05:32

import ckeditor.fields
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Error_page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.IntegerField(null=True)),
                ('Page_name', models.CharField(max_length=100, null=True)),
                ('Page_url', models.CharField(max_length=100, null=True)),
                ('Page_id', models.IntegerField(null=True)),
                ('Error_type', models.CharField(max_length=100, null=True)),
                ('View_count', models.IntegerField(null=True)),
                ('Status', models.CharField(choices=[('Solved', 'Solved'), ('Unsolved', 'Unsolved')], max_length=100, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Other_page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.IntegerField(null=True)),
                ('Page_name', models.CharField(max_length=100, null=True)),
                ('Page_url', models.CharField(max_length=100, null=True)),
                ('Description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('Meta_title', models.CharField(max_length=100, null=True)),
                ('Meta_description', models.TextField(max_length=100, null=True)),
                ('Meta_tag', models.CharField(max_length=100, null=True)),
                ('Page_maintained_by', models.CharField(max_length=100, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Total_page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.IntegerField(null=True)),
                ('Page_name', models.CharField(max_length=100, null=True)),
                ('Page_url', models.CharField(max_length=100, null=True)),
                ('Error_Page', models.CharField(max_length=100, null=True)),
                ('Today_page', models.IntegerField(null=True)),
                ('view_count', models.IntegerField(null=True)),
                ('Bounce_rate', models.IntegerField(null=True)),
                ('Page_maintained_by', models.CharField(max_length=100, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trending_page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.IntegerField(null=True)),
                ('Page_id', models.IntegerField(null=True)),
                ('Page_name', models.CharField(max_length=100, null=True)),
                ('Page_url', models.CharField(max_length=100, null=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None)),
                ('view_count', models.IntegerField(null=True)),
                ('Total_page', models.IntegerField(null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('activity', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
