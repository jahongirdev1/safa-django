from django.db import models
from ckeditor.fields import RichTextField


class Language(models.Model):
    code = models.CharField(max_length=10, unique=True)
    title = models.CharField(max_length=200)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Company(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    why_collecting = models.CharField(max_length=200)
    image = models.ImageField(upload_to='companies/')
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Post(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/')
    title = models.CharField(max_length=300)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title


from django.db import models


class Note(models.Model):
    TYPE_CHOICES = [
        ('normal', 'Обычный'),
        ('medium', 'Средний'),
        ('urgent', 'Срочный'),
        ('very_urgent', 'Очень срочный'),
    ]

    language = models.ForeignKey('Language', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='notes/')
    title = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    content = models.TextField()
    goal_money = models.FloatField()
    collected_money = models.FloatField()
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='normal')
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class MaterialsStatus(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name="Язык")
    title = models.CharField(max_length=100, verbose_name="Семейное положение")
    status = models.IntegerField(default=0, verbose_name="Статус")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Семейное положение"
        verbose_name_plural = "Семейные положения"


class HelpCategory(models.Model):
    title = models.CharField(max_length=250, verbose_name="Название категории помощи")
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True)
    is_other = models.BooleanField(default=False, verbose_name="Является 'Другое'")
    status = models.IntegerField(default=0, verbose_name="Статус")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория помощи"
        verbose_name_plural = "Категории помощи"


class HelpRequest(models.Model):
    name = models.CharField(max_length=200, verbose_name="Имя")
    surname = models.CharField(max_length=200, verbose_name="Фамилия")
    age = models.IntegerField(default=0, blank=True, verbose_name="Возраст")
    email = models.EmailField(blank=True, null=True, verbose_name="Электронная почта")
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефона")
    material_status = models.ForeignKey(MaterialsStatus, on_delete=models.CASCADE, verbose_name="Семейное положение")
    help_category = models.ForeignKey(HelpCategory, on_delete=models.CASCADE, verbose_name="Категория помощи",blank=True, null=True)
    other_category = models.CharField(max_length=250, blank=True, null=True, verbose_name="Другая категория")
    child_in_fam = models.IntegerField(default=0, blank=True, verbose_name="Количество детей")
    address = models.CharField(max_length=200, verbose_name="Адрес")
    iin = models.CharField(max_length=12, blank=True, verbose_name="ИИН")
    why_need_help = models.TextField(verbose_name="Причина обращения за помощью")
    file = models.FileField(upload_to='uploads/', blank=True, verbose_name="Изображение")
    money = models.FloatField()
    status = models.IntegerField(default=0, verbose_name="Статус")

    def __str__(self):
        return f"{self.name} {self.surname}"

    class Meta:
        verbose_name = "Заявка на помощь"
        verbose_name_plural = "Заявки на помощь"