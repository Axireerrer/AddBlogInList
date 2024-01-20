from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse


def validate_age(value):
    if value not in range(18, 80):
        raise ValidationError("Неверно веденный возраст!!!")
    return value


class FamousPerson(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    surname = models.CharField(max_length=30, verbose_name='Фамилия')
    age = models.IntegerField(validators=[validate_age], verbose_name='Возраст', blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    image = models.ImageField(verbose_name='Фото', blank=True)
    slug = models.SlugField(max_length=20, verbose_name='URL', null=True, unique=True)
    time_creating = models.DateTimeField(auto_now=True, verbose_name='Время создания')
    category = models.ForeignKey('CategoryPerson', on_delete=models.PROTECT, verbose_name='Категория')

    class Meta:
        ordering = ['-time_creating']
        indexes = [
            models.Index(fields=['slug', '-time_creating'])
        ]
        verbose_name = 'Известные люди'
        verbose_name_plural = 'Известные люди'

    def __str__(self):
        return self.slug

    objects = models.Manager()


class CategoryPerson(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=20, db_index=True, unique=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('persons', kwargs={'some_slug': self.slug})

    objects = models.Manager()