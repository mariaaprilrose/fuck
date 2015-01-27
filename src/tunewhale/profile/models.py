import os
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

def update_avatar_filename(instance, filename):
    extension = filename.split('.')[-1]
    filename = '{0}.{1}'.format('avatar', extension)
    path = '{0}{1}'.format(settings.USER_UPLOAD_PATH,
                           instance.user.username)
    return os.path.join(path, filename)

def update_cover_filename(instance, filename):
    extension = filename.split('.')[-1]
    filename = '{0}.{1}'.format('cover', extension)
    path = '{0}{1}'.format(settings.USER_UPLOAD_PATH,
                           instance.user.username)
    return os.path.join(path, filename)

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    date_registered = models.DateField(auto_now_add=True)
    location = models.CharField(max_length=50, blank=True)
    status = models.ImageField(upload_to=settings.STATUS_UPLOAD_PATH,
                               default=settings.BABYWHALE_IMG_PATH)
    music_interests = models.TextField(blank=True)
    music_genres = models.TextField(blank=True)
    best_song_ever = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to=update_avatar_filename,
                               default=settings.DEFAULT_AVATAR_PATH)
    cover = models.ImageField(upload_to=update_cover_filename,
                                    default=settings.DEFAULT_COVER_PATH)
    followers = models.ManyToManyField(User, blank=True,
                                       related_name='followers')
    following = models.ManyToManyField(User, blank=True,
                                       related_name='following')
    def __unicode__(self):
        return self.user.username
    def get_avatar_url(self):
        filename = self.avatar.url.split('/')
        new_filename = ''
        for w in filename[2:]:
            new_filename += w + '/'
        return new_filename
    def get_cover_url(self):
        filename = self.cover.url.split('/')
        new_filename = ''
        for w in filename[2:]:
            new_filename += w + '/'
        return new_filename
    def get_status_url(self):
        filename = self.status.url.split('/')
        new_filename = ''
        for w in filename[2:]:
            new_filename += w + '/'
        return new_filename
    def followers_count(self):
        # possible additions in the future:
        #   - display numbers with commas, e.g. 15,000
        #   - as of now, the template can only display 8 digits with commas, 9 digits without commas
        #   - display millions (and higher) with letter, e.g. 1.2M, 15M
        count = 0
        for user in self.followers.all():
            count += 1
        return count