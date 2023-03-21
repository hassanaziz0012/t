from django.db import models
from django.utils import timezone
from users.models import Comment, Profile


# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=400)
    creation_date = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    file = models.FileField(upload_to='videos')
    preview = models.FileField(upload_to='videos/previews', null=True, blank=True)
    thumbnail = models.ImageField(upload_to='thumbnails', null=True)

    is_3d = models.BooleanField(default=False)
    free = models.BooleanField(default=False)

    alternative_qualities = models.ManyToManyField('AlternativeQualityVideo', blank=True)

    pornstars = models.ManyToManyField('users.Pornstar', blank=True)

    likes = models.ManyToManyField(Profile, blank=True, related_name='video_likes')
    comments = models.ManyToManyField(Comment, blank=True, related_name='video_comments')

    def __str__(self) -> str:
        return f'{self.title}'

    def __repr__(self) -> str:
        return f'<Video: {self.title}>'


class AlternativeQualityVideo(models.Model):
    label = models.CharField(max_length=100)
    file = models.FileField(upload_to='videos/alternatives')

    def __str__(self) -> str:
        return f'{self.label}'

    def __repr__(self) -> str:
        return f'<AlternativeQualityVideo: {self.label}>'


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return f'{self.name}'

    def __repr__(self) -> str:
        return f'<Category: {self.name}>'