# from django.db import models
#
# class User(models.Model):
#     name = models.CharField(max_length=255)
#     number = models.CharField(max_length=50)
#     IT_DIRECTIONS = [
#         ('backend', 'Backend'),
#         ('frontend', 'Frontend'),
#         # ('web', 'Web Development'),
#         # ('data', 'Data Science'),
#         # ('devops', 'DevOps'),
#         # ('ml', 'Machine Learning'),
#         # ('cloud', 'Cloud Computing'),
#         # ('mobile', 'Mobile Development'),
#         # ('network', 'Network Engineering'),
#         # Добавьте другие направления
#     ]
#     connected = models.BooleanField(default=False)
#     interviewed = models.BooleanField(default=False)
#     is_deleted = models.BooleanField(default=False)
#     direction = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.name
#
from django.db import models

class User(models.Model):
    # Ваши другие поля
    IT_DIRECTIONS = [
        ('backend', 'Backend'),
        ('frontend', 'Frontend'),
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

    def __str__(self):
        return self.name
