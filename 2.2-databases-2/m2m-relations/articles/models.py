from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    scopes = models.ManyToManyField(Tag, through='ArticleTag', verbose_name='Разделы')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class ArticleTag(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name='РАЗДЕЛ')
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.article} - {self.tag}'
