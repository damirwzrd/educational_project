import datetime

from django.db import models


# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название курса')
    description = models.TextField(verbose_name='Описание курса')
    lessons_count = models.IntegerField(verbose_name='Количество уроков')
    lesson_duration = models.FloatField(verbose_name='Длительность урока в минутах')
    course_logo = models.ImageField(verbose_name='Логотип курса')

    def __str__(self):
        return f"{self.name}: {self.description}"


class Student(models.Model):
    date_of_birth = models.DateField(verbose_name='День рождения', default=datetime.date.today())
    course = models.ForeignKey(Course, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.course.name}: {self.date_of_birth}"


class Comment(models.Model):
    author = models.CharField(max_length=30, verbose_name="Комментатор")
    comment_text = models.TextField(verbose_name="Текст комментария")
    created_date = models.DateField(auto_now_add=True, verbose_name="Дата создания комментария")
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author}: {self.created_date}"

