from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=70, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='images', verbose_name='Изображение')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')


    TYPE = [
        ('man', 'мужчинам'),
        ('girl', 'женщинам'),
        ('child', 'детям'),
    ]
    type = models.CharField(choices=TYPE, max_length=5, default='man', verbose_name='тип')

    def __str__(self):
        return self.title

