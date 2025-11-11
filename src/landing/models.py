from django.db import models


class PortfolioItem(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва")
    category = models.ForeignKey('PortfolioCategory', on_delete=models.PROTECT, verbose_name='Категорія')
    client = models.CharField(max_length=100, blank=True, null=True, verbose_name="Клієнт")
    description = models.TextField(blank=True, null=True, verbose_name="Опис")
    short_description = models.TextField(blank=True, null=True, verbose_name="Короткий опис")
    source = models.URLField(blank=True, null=True, verbose_name="Посилання")
    image = models.ImageField(upload_to='my_images/', verbose_name="Зображення")
    alt_text = models.TextField(blank=True, null=True, verbose_name="Альтернативний текст")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Оновлено")
    is_published = models.BooleanField(default=False, verbose_name="Опубліковано")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Роботи'


class PortfolioCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва категорії", unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Категорії'
