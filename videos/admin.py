from django.contrib import admin
from videos.models import AlternativeQualityVideo, Category, Video


# Register your models here.
@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'creation_date', 'category', '_likes', '_comments')
    exclude = ('likes', 'comments')

    def _likes(self, video):
        return video.likes.count()

    def _comments(self, video):
        return video.comments.count()


@admin.register(AlternativeQualityVideo)
class AlternativeQualityVideoAdmin(admin.ModelAdmin):
    list_display = ('video', 'label', 'file')

    def video(self, alt):
        vid_obj = Video.objects.filter(alternative_qualities__contains=self)
        if vid_obj.exists():
            return vid_obj.title
        else:
            return None


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)