from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from decimal import Decimal
from django.utils import timezone

class Category(models.Model):
    CATEGORY_TYPES = [
        ('income', 'Доход'),
        ('expense', 'Расход'),
    ]
    
    name = models.CharField(max_length=100, verbose_name='Название категории')
    type = models.CharField(
        max_length=10, 
        choices=CATEGORY_TYPES, 
        default='expense',
        verbose_name='Тип категории'
    )
    parent = models.ForeignKey(
        'self', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        related_name='subcategories',
        verbose_name='Родительская категория'
    )
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True,
        verbose_name='Пользователь'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['type', 'name']
    
    def __str__(self):
        return f"{self.type}: {self.name}"

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('income', 'Доход'),
        ('expense', 'Расход'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    amount = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        validators=[MinValueValidator(Decimal('0.01'))],
        verbose_name='Сумма'
    )
    type = models.CharField(
        max_length=10, 
        choices=TRANSACTION_TYPES, 
        verbose_name='Тип операции'
    )
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        verbose_name='Категория'
    )
    description = models.TextField(max_length=500, blank=True, verbose_name='Описание')
    date = models.DateTimeField(
        verbose_name='Дата операции',
        default=timezone.now
        )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    
    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'
        ordering = ['-date']
        indexes = [
            models.Index(fields=['user', 'date']),
            models.Index(fields=['user', 'type']),
            models.Index(fields=['user', 'category']),
        ]
    
    def __str__(self):
        return f"{self.user.username}: {self.type} {self.amount} ({self.date.strftime('%d.%m.%Y')})"

class Budget(models.Model):
    PERIOD_CHOICES = [
        ('daily', 'Ежедневный'),
        ('weekly', 'Еженедельный'),
        ('monthly', 'Ежемесячный'),
        ('yearly', 'Ежегодный'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        verbose_name='Категория'
    )
    amount = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        validators=[MinValueValidator(Decimal('0.01'))],
        verbose_name='Сумма бюджета'
    )
    period = models.CharField(
        max_length=10, 
        choices=PERIOD_CHOICES, 
        default='monthly',
        verbose_name='Период'
    )
    start_date = models.DateField(verbose_name='Начало периода')
    end_date = models.DateField(verbose_name='Конец периода')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    
    class Meta:
        verbose_name = 'Бюджет'
        verbose_name_plural = 'Бюджеты'
        unique_together = ['user', 'category', 'period', 'start_date']
        ordering = ['-start_date', 'category']
    
    def __str__(self):
        return f"{self.user.username}: {self.category.name} - {self.amount} ({self.period})"