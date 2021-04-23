from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


User = get_user_model()


class Group(models.Model):
    class Meta:
        ordering = ['-title']

    title = models.CharField(
        verbose_name='Группа',
        max_length=200,
        help_text='Введите название группы'
    )

    slug = models.SlugField(unique=True)
    description = models.TextField(
        verbose_name='Описание группы',
        help_text='Описание группы')

    def __str__(self):
        return self.title


class Post(models.Model):

    class Meta:
        ordering = ['-pub_date']

    text = models.TextField(
        verbose_name='Текст',
        help_text='Введите новость')

    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True,
        db_index=True)

    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='posts')

    group = models.ForeignKey(
        Group,
        verbose_name='Группа',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='posts')

    # image = models.ImageField(
    #     verbose_name='Картинка',
    #     upload_to='posts/',
    #     blank=True,
    #     null=True)

    def __str__(self):
        return self.text[:15]
