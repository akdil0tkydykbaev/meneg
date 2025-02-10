from django.db import models


class Trainer(models.Model):
    name = models.CharField(max_length=100)
    direction = models.CharField(max_length=100)

class User(models.Model):
    # Ваши другие поля
    IT_DIRECTIONS = [
        ('Backend', 'Backend'),
        ('Frontend', 'Frontend'),
        # ('web', 'Web Development'),
        # ('data', 'Data Science'),
        # ('devops', 'DevOps'),
        # ('ml', 'Machine Learning'),
        # ('cloud', 'Cloud Computing'),
        # ('mobile', 'Mobile Development'),
        # ('network', 'Network Engineering'),
        # Добавьте другие направления
    ]

    name = models.CharField(max_length=100)
    number = models.CharField(max_length=50)
    direction = models.CharField(max_length=20, choices=IT_DIRECTIONS)
    is_deleted = models.BooleanField(default=False)
    connected = models.BooleanField(default=False)
    interviewed = models.BooleanField(default=False)
    interview_date = models.DateTimeField(null=True, blank=True)  # Дата и время собеседования

    def __str__(self):
        return self.name

    class Trainer(models.Model):
        name = models.CharField(max_length=255)
        direction = models.CharField(max_length=255)

        def __str__(self):
            return f"{self.name} ({self.direction})"


    class User(models.Model):
        name = models.CharField(max_length=100)
        number = models.CharField(max_length=15)
        direction = models.CharField(max_length=100)
        interview_date = models.DateTimeField(null=True, blank=True)  # Дата и время собеседования
        trainer = models.ForeignKey(Trainer, null=True, blank=True, on_delete=models.SET_NULL)  # Назначенный тренер



