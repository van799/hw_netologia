from django.db import models


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='Название модели телефона')
    price = models.IntegerField(verbose_name='Цена телфона')
    image = models.URLField()
    release_date = models.DateField(auto_now=False, verbose_name='Дата релиза')
    lte_exists = models.BooleanField(verbose_name='Наличие LTE')
    slug = models.SlugField(unique=True, verbose_name='URL адрес')

    def __str__(self):
        return f"{self.name}"
