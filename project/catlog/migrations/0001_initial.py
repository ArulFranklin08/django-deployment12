# Generated by Django 2.2.5 on 2020-11-12 05:32

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.IntegerField(null=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('image_url', models.CharField(max_length=100, null=True)),
                ('image_alt_tag', models.CharField(max_length=100, null=True)),
                ('brand_video', models.FileField(blank=True, upload_to='videos/')),
                ('video_url', models.CharField(max_length=100, null=True)),
                ('video_alt_tag', models.CharField(max_length=100, null=True)),
                ('meta_title', models.CharField(max_length=100, null=True)),
                ('meta_keywords', models.CharField(max_length=100, null=True)),
                ('meta_description', models.TextField(null=True)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.IntegerField(null=True)),
                ('category_type', models.CharField(max_length=30)),
                ('category_name', models.CharField(max_length=100, null=True)),
                ('category_url', models.CharField(max_length=100, null=True)),
                ('category_image', models.ImageField(blank=True, upload_to='images/')),
                ('image_url', models.CharField(max_length=100, null=True)),
                ('image_alt_tag', models.CharField(max_length=100, null=True)),
                ('category_video', models.FileField(blank=True, upload_to='videos/')),
                ('video_alt_tag', models.CharField(max_length=100, null=True)),
                ('video_url', models.CharField(max_length=100, null=True)),
                ('meta_title', models.CharField(max_length=100, null=True)),
                ('meta_keyword', models.CharField(max_length=100, null=True)),
                ('meta_description', models.TextField(null=True)),
                ('description', models.TextField(null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sub_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.IntegerField(null=True)),
                ('subcategory_name', models.CharField(max_length=100, null=True)),
                ('subcategory_url', models.CharField(max_length=100, null=True)),
                ('subcategory_image', models.ImageField(blank=True, upload_to='images/')),
                ('image_url', models.CharField(max_length=100, null=True)),
                ('image_alt_tag', models.CharField(max_length=100, null=True)),
                ('video_upload', models.FileField(blank=True, upload_to='videos/')),
                ('video_alt_tag', models.CharField(max_length=100, null=True)),
                ('video_url', models.CharField(max_length=100, null=True)),
                ('meta_title', models.CharField(max_length=100, null=True)),
                ('meta_keyword', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(null=True)),
                ('meta_description', models.TextField(null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('category_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catlog.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.IntegerField(null=True)),
                ('product_name', models.CharField(max_length=100, null=True)),
                ('prescription', models.CharField(max_length=100, null=True)),
                ('product_url', models.CharField(max_length=100, null=True)),
                ('product_image', models.ImageField(blank=True, upload_to='images/')),
                ('image_url', models.CharField(max_length=100, null=True)),
                ('video_upload', models.FileField(blank=True, upload_to='videos/')),
                ('video_url', models.CharField(max_length=100, null=True)),
                ('video_alt_tag', models.CharField(max_length=100, null=True)),
                ('composition', models.CharField(max_length=100, null=True)),
                ('manufactuer', models.CharField(max_length=100, null=True)),
                ('form', models.CharField(max_length=100, null=True)),
                ('strength', models.IntegerField()),
                ('package', models.CharField(max_length=100, null=True)),
                ('packing', models.CharField(max_length=100, null=True)),
                ('mrp', models.IntegerField(null=True)),
                ('available_stock', models.CharField(max_length=100, null=True)),
                ('percentage', models.IntegerField(null=True)),
                ('meta_title', models.CharField(max_length=100, null=True)),
                ('meta_keyword', models.CharField(max_length=100, null=True)),
                ('meta_description', models.TextField(null=True)),
                ('medicine_information', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('therapeutic_classification', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('schedule', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('mechanism_of_action', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('contraindication', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('side_effects', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('faqs', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('precautions_general_warnings', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('metabolism', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('elimination', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('general_instructions', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('drug_interaction', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('dosage', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('storage_disposal', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('fast_tag', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('references', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('image_alt_tag', models.CharField(max_length=100, null=True)),
                ('content_written_by', models.CharField(max_length=100, null=True)),
                ('content_reviewed_by', models.CharField(max_length=100, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catlog.Brand')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catlog.Category')),
                ('sub_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catlog.Sub_category')),
            ],
        ),
    ]
