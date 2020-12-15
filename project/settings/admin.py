from django.contrib import admin
from .models import *
from .models import Post, Post_Image
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class Main_sliderAdmin(ImportExportModelAdmin):
    list_display = ['sno','home_slider', 'image_alt_tag']
    list_filter = ['home_slider']

class A_side_bannerAdmin(ImportExportModelAdmin):
    list_display = ['sno','category_name', 'banner_images']
    list_filter = ['category_name']

class Drug_carts_serviceAdmin(ImportExportModelAdmin):
    list_display = ['sno','title', 'image']
    list_filter = ['title']

class Special_careAdmin(ImportExportModelAdmin):
    list_display = ['sno','title', 'image']
    list_filter = ['title']

class ClinicAdmin(ImportExportModelAdmin):
    list_display = ['sno','title', 'image']
    list_filter = ['title']

class Pick_opportunityAdmin(ImportExportModelAdmin):
    list_display = ['sno','title', 'image']
    list_filter = ['title']

class Post_ImageAdmin(admin.StackedInline):
    model=Post_Image

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [Post_ImageAdmin]

    class Meta:
        model = Post

@admin.register(Post_Image)
class Post_ImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Main_slider, Main_sliderAdmin)
admin.site.register(A_side_banner, A_side_bannerAdmin)
admin.site.register(Drug_carts_service, Drug_carts_serviceAdmin)
admin.site.register(Special_care, Special_careAdmin)
admin.site.register(Clinic, ClinicAdmin)
admin.site.register(Pick_opportunity, Pick_opportunityAdmin)
