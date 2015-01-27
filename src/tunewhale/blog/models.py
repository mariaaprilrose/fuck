import os, random, re, string
from django.conf import settings
from django.db import models

def update_blog_picture(instance, filename):
    extension = filename.split('.')[-1]
    filename = '{0}.{1}'.format('picture', extension)
    folder_name = id_generator()
    path = '{0}{1}'.format(settings.BLOG_PATH, folder_name)
    return os.path.join(path, filename)

#to distinguish between blogs, default size is 24 characters
def id_generator(size=24, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

class Blog(models.Model):
    title = models.CharField(max_length=100)
    date_published = models.DateTimeField(auto_now_add=True)
    comments = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    picture = models.ImageField(upload_to=update_blog_picture, blank=True)
    content = models.TextField()
    def __unicode__(self):
        return self.title
    def convert_title(self):
        return self.title.replace(' ', '_')
    def get_picture_url(self):
        filename = self.picture.url.split('/')
        new_filename = ''
        for w in filename[2:]:
            new_filename += w + '/'
        return new_filename