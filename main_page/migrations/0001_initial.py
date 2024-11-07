# Generated by Django 4.2.16 on 2024-11-07 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='book/', verbose_name='Заргузите картинку')),
                ('title', models.CharField(max_length=100, verbose_name='Укажите название книги')),
                ('description', models.TextField(default='Интересная книга', null=True, verbose_name='Укажите описание к книге')),
                ('price', models.FloatField(verbose_name='Укажите цену книги')),
                ('release_date', models.DateField(verbose_name='Укажите дату выхода')),
                ('genre', models.CharField(choices=[('Детективы', 'Детективы'), ('Триллеры', 'Триллеры'), ('Новелла', 'Новелла')], default='Триллер', max_length=100)),
                ('author', models.CharField(max_length=100, verbose_name='Укажите имя автора')),
                ('audio', models.URLField(verbose_name='Вставьте ссылку на аудио книгу с YouTube')),
                ('email', models.EmailField(max_length=254, verbose_name='Укажите почту автора')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
    ]