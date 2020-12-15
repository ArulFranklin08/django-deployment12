from django.db import models

#from mptt.fields import TreeForeignKey
#from mptt.models import MPTTModel
from ckeditor.fields import RichTextField


# Create your models here.
class Brand(models.Model):
    sno = models.IntegerField(null=True)
    name = models.CharField(max_length=100, null=True)
    image = models.ImageField(blank=True,upload_to='images/')
    image_url = models.CharField(max_length=100, null=True)
    image_alt_tag = models.CharField(max_length=100, null=True)
    brand_video = models.FileField(blank=True,upload_to='videos/')
    video_url = models.CharField(max_length=100, null=True)
    video_alt_tag = models.CharField(max_length=100, null=True)
    meta_title = models.CharField(max_length=100, null=True)
    meta_keywords = models.CharField(max_length=100, null=True)
    meta_description = models.TextField(null=True)
    description = RichTextField(blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    #parent = TreeForeignKey('self',on_delete=models.CASCADE, null=True, blank=True,related_name='children')
    sno = models.IntegerField(null=True)
    category_type = models.CharField(max_length=30)
    category_name = models.CharField(max_length=100, null=True)
    category_url = models.CharField(max_length=100, null=True)
    category_image = models.ImageField(blank=True,upload_to='images/')
    image_url = models.CharField(max_length=100, null=True)
    image_alt_tag = models.CharField(max_length=100, null=True)
    category_video = models.FileField(blank=True,upload_to='videos/')
    video_alt_tag = models.CharField(max_length=100, null=True)
    video_url = models.CharField(max_length=100, null=True)
    meta_title = models.CharField(max_length=100, null=True)
    meta_keyword = models.CharField(max_length=100, null=True)
    meta_description = models.TextField(null=True)
    description = models.TextField(null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name


class Sub_category(models.Model):
    sno = models.IntegerField(null=True)
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    subcategory_name = models.CharField(max_length=100, null=True)
    subcategory_url = models.CharField(max_length=100, null=True)
    subcategory_image = models.ImageField(blank=True,upload_to='images/')
    image_url = models.CharField(max_length=100, null=True)
    image_alt_tag = models.CharField(max_length=100, null=True)
    video_upload = models.FileField(blank=True,upload_to='videos/')
    video_alt_tag = models.CharField(max_length=100, null=True)
    video_url = models.CharField(max_length=100, null=True)
    meta_title = models.CharField(max_length=100, null=True)
    meta_keyword = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    meta_description = models.TextField(null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subcategory_name


class Product(models.Model):
    sno = models.IntegerField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    sub_category = models.ForeignKey(Sub_category, on_delete=models.CASCADE, null=True, blank=True)
    product_name = models.CharField(max_length=100, null=True)
    prescription = models.CharField(max_length=100, null=True)
    product_url = models.CharField(max_length=100, null=True)
    product_image = models.ImageField(blank=True,upload_to='images/')
    image_url = models.CharField(max_length=100, null=True)
    image_alt_tag = models.CharField(max_length=100, null=True)
    video_upload = models.FileField(blank=True,upload_to='videos/')
    video_url = models.CharField(max_length=100, null=True)
    video_alt_tag = models.CharField(max_length=100, null=True)
    composition = models.CharField(max_length=100, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)
    manufactuer = models.CharField(max_length=100, null=True)
    form = models.CharField(max_length=100, null=True)
    strength = models.IntegerField()
    package = models.CharField(max_length=100, null=True)
    packing = models.CharField(max_length=100, null=True)
    mrp = models.IntegerField(null=True)
    available_stock = models.CharField(max_length=100, null=True)
    percentage = models.IntegerField(null=True)
    meta_title = models.CharField(max_length=100, null=True)
    meta_keyword = models.CharField(max_length=100, null=True)
    meta_description = models.TextField(null=True)
    medicine_information = RichTextField(blank=True, null=True)
    therapeutic_classification = RichTextField(blank=True, null=True)
    schedule = RichTextField(blank=True, null=True)
    mechanism_of_action = RichTextField(blank=True, null=True)
    contraindication = RichTextField(blank=True, null=True)
    side_effects = RichTextField(blank=True, null=True)
    faqs = RichTextField(blank=True, null=True)
    precautions_general_warnings = RichTextField(blank=True, null=True)
    metabolism = RichTextField(blank=True, null=True)
    elimination = RichTextField(blank=True, null=True)
    general_instructions = RichTextField(blank=True, null=True)
    drug_interaction = RichTextField(blank=True, null=True)
    dosage = RichTextField(blank=True, null=True)
    storage_disposal = RichTextField(blank=True, null=True)
    fast_tag = RichTextField(blank=True, null=True)
    references = RichTextField(blank=True, null=True)
    name = models.CharField(max_length=100, null=True)
    image = models.ImageField(blank=True,upload_to='images/')
    image_alt_tag = models.CharField(max_length=100, null=True)
    content_written_by = models.CharField(max_length=100, null=True)
    content_reviewed_by = models.CharField(max_length=100, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name
