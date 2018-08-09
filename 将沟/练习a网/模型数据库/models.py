from django.db import models


class 练习a网表(models.Model):
    名字 = models.CharField(max_length=30)
    年龄 = models.IntegerField()