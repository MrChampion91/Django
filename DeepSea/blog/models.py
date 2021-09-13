from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name ="название")
    text = models.TextField(verbose_name="текст")

    def __str__(self):
        return self.title

