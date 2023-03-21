from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe


# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subscription = models.ForeignKey("subscriptions.Subscription", blank=True, null=True, on_delete=models.CASCADE, related_name="subscription")
    def __str__(self) -> str:
        return f'{self.user.username}'

    def __repr__(self) -> str:
        return f'<Profile: {self.user.username}>'


class Comment(models.Model):
    video = models.ForeignKey('videos.Video', on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.TextField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.video.comments.filter(pk=self.pk).exists():
            self.video.comments.add(self)
            self.video.save()

        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.author}\'s Comment'

    def __repr__(self) -> str:
        return f'<Comment: {self.author}>'


class Pornstar(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="pornstars")

    def image_tag(self):
        return mark_safe('<img src="%s" / width=100 height=100>' % self.image.url)

    def __str__(self) -> str:
        return f'{self.name}'

    def __repr__(self) -> str:
        return f'<Pornstar: {self.name}>'
