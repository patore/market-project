from django.contrib import admin

from .models import Product, Thumbnail, MyProducts

class ThumbnailInline(admin.TabularInline):
	model = Thumbnail

class ProductAdmin(admin.ModelAdmin):
	inlines = [ThumbnailInline]
	list_display = ["__unicode__", "media", "description", "price", "sale_price"]
	search_fields = ["title", "description"]
	list_filter = ["price"]
	list_editable = ["sale_price"]
	class Meta:
		model = Product

admin.site.register(Product, ProductAdmin)

admin.site.register(Thumbnail)

admin.site.register(MyProducts)