from django.contrib import admin
from .models import Category, Transaction, Budget

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'parent', 'user', 'created_at')
    list_filter = ('type', 'parent')
    search_fields = ('name',)
    list_select_related = ('parent', 'user')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'type', 'category', 'date', 'created_at')
    list_filter = ('type', 'category', 'date')
    search_fields = ('description', 'user__username')
    date_hierarchy = 'date'
    list_select_related = ('user', 'category')

@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'amount', 'period', 'start_date', 'end_date')
    list_filter = ('period', 'start_date')
    search_fields = ('user__username', 'category__name')
    list_select_related = ('user', 'category')