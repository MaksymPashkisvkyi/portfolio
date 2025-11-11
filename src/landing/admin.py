from django.contrib import admin

from .models import PortfolioItem, PortfolioCategory


@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'client', 'description', 'short_description', 'source', 'image', 'alt_text',
                    'created_at', 'updated_at',
                    'updated_at', 'is_published')


@admin.register(PortfolioCategory)
class PortfolioCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
