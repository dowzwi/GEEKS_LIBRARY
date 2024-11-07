from django.db import models

class books(models.Model):
    GENRE_CHOICES = (
        ('Детективы','Детективы'),
        ('Триллеры','Триллеры'),
        ('Манга','Манга')
    )
    image = models.ImageField(upload_to='book/', verbose_name='Заргузите картинку')
    title = models.CharField(max_length=100, verbose_name='Укажите название книги')
    description = models.TextField(verbose_name='Укажите описание к книге', default='Интересная книга', null=True)
    price = models.FloatField(verbose_name='Укажите цену книги')
    release_date = models.DateField(verbose_name='Укажите дату выхода')
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES,
                             default='Триллер')
    author = models.CharField(max_length=100, verbose_name='Укажите имя автора')
    audio = models.URLField(verbose_name='Вставьте ссылку на аудио книгу с YouTube')
    email = models.EmailField(verbose_name='Укажите почту автора')


    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return f'{self.title}-{self.price}$'