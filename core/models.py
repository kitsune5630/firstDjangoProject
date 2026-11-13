from django.db import models

# put there for auto html generation plus db generation

class Article(models.Model):
    title = models.CharField(
        verbose_name="Заголовок",
        unique=True,
        max_length=200,
        blank=True,
        null=True,
        default="Без названия",
        help_text="До 200 символов",
        db_index=True,
    )
    slug = models.CharField(
        verbose_name="Slug",
        unique=True,
        max_length=100,
        blank=True,
    )
    author = models.CharField(
        verbose_name="Автор",
        default="Анон"
    )
    body = models.CharField(
        verbose_name="Основное",
    )
    created_at = models.DateTimeField(
        verbose_name="Создано",
        deafult="01.01.2000"
    )
    tags = models.ManyToManyField(
        verbose_name="Теги",
        
    )

class Tags(models.Model):
    name = models.CharField()
    slug = models.CharField()

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.CharField()
    text = models.TextField()
    created_at = models.DateTimeField()
    