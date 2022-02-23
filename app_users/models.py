from django.db import models
from django.contrib.auth.models import User


class News(models.Model):

    title = models.CharField(max_length=200, verbose_name="Заголовок")
    text = models.TextField(max_length=1000, default="", verbose_name="Текст новости")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    update = models.DateTimeField(auto_now=True, verbose_name="Обновлено")
    my_image = models.ImageField(null=True, blank=True, upload_to="images/")
    author = models.ForeignKey("Profile",default=None, null=True,  on_delete=models.CASCADE,
                               related_name="news", verbose_name="Автор")

    class Meta:
        db_table = "news"
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ["-created"]

    def __str__(self):
        return self.title


class Profile(models.Model):

    user = models.OneToOneField(User,  on_delete=models.CASCADE, null=True)
    city = models.CharField(max_length=30, null=True, blank=True, verbose_name="Город")
    tel = models.CharField(max_length=15, null=True, blank=True, verbose_name="Телефон")
    verify = models.BooleanField(default=False, verbose_name="Режим верификации")
    moderator = models.BooleanField(default=False, verbose_name="Модератор")
    count = models.IntegerField(default=0, verbose_name="Количество статей")

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

    def __str__(self):
        return self.user.username


class Coments(models.Model):

    user_name = models.CharField(max_length=50, verbose_name="Ник")
    text = models.TextField(max_length=700, default="", verbose_name="коментарий")
    news = models.ForeignKey("News", default=None, null=True, on_delete=models.CASCADE,
                             related_name="coments", verbose_name="Новости")
    user = models.ForeignKey(User ,default=None, null=True, on_delete=models.CASCADE,
                            verbose_name="Пользователь")


    class Meta:
        db_table = "coments"
        verbose_name = "Коментарии"
        verbose_name_plural = "Коментарии"

    def __str__(self):
        return self.text