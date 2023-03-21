from django.db import models

# Create your models here.
class StaticImage(models.Model):
    name = models.CharField(max_length=100)
    file = models.ImageField(upload_to='static-images', null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.name}'

    def __repr__(self) -> str:
        return f'<StaticImage: {self.name}>'
        