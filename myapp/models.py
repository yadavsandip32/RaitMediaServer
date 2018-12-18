from django.db import models
from random import randint

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


#
# def user_directory_path(instance, filename):
#     # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
#     return '{0}'.format(random.random())

class Document(models.Model):
    id = models.IntegerField(default = randint(10**3, (10**4)), unique=True,primary_key=True)
    docfile = models.FileField(upload_to='documents')
    like = models.IntegerField(default = 0)
    views = models.IntegerField(default = 0)

# class Document(models.Model):

#     x = user_directory_path
#     docfile = models.FileField(upload_to=documents)
    # image_thumbnail = ImageSpecField(source='docfile',
    #                                  processors=[ResizeToFill(100, 50)],
    #                                  format='JPEG')
# from django.db import models
#
# from videokit.models import VideoField
#
# class Document(models.Model):
#     docfile = VideoField( upload_to = 'document', null = True, blank = True,
#                         width_field = 'video_width', height_field = 'video_height',
#                         rotation_field = 'video_rotation',
#                         mimetype_field = 'video_mimetype',
#                         duration_field = 'video_duration',
#                         thumbnail_field = 'video_thumbnail')
#     video_width = models.IntegerField(null = True, blank = True)
#     video_height = models.IntegerField(null = True, blank = True)
#     video_rotation = models.FloatField(null = True, blank = True)
#     video_mimetype = models.CharField(max_length = 32, null = True, blank = True)
#     video_duration = models.IntegerField(null = True, blank = True)
#     video_thumbnail = models.ImageField(null = True, blank = True)