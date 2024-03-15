from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='images', verbose_name='Изображение')
    price = models.DecimalField(max_digits=50, decimal_places=2, verbose_name='Цена')


    TYPE = [
        ('nike', 'Nike'),
        ('jordan', 'Jordan'),
        ('new balance', 'New balance'),
        ('adidas', 'Adidas')
    ]
    type = models.CharField(choices=TYPE, max_length=50, default='nike', verbose_name='тип')


    def __str__(self):
        return self.title