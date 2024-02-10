from django.db import models
from django.utils import timezone

from django.contrib.auth import get_user_model
User = get_user_model()


def user_directory_path(instance, filename):
	return 'users/socialposts/{0}'.format(filename)

# def dm_directory_path(instance, filename):
# 	return 'users/messages/{0}'.format(filename)


class SocialPost(models.Model):
    shared_body = models.TextField(blank=True, null=True)
    shared_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='+')
    shared_on = models.DateTimeField(blank=True, null=True)
    body=models.TextField()
    image = models.ManyToManyField('Image', blank=True)#'Image' hace referencia al modelo Image
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='social_post_author')
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='dislikes')


class SocialComment(models.Model):
    comment = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='social_comment_author')
    post = models.ForeignKey('SocialPost', on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank=True, related_name='comment_likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='comment_dislikes')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='+')

    @property
    def children(self):
        return SocialComment.objects.filter(parent=self).order_by('-created_on').all()

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False



class Image(models.Model):
    image = models.ImageField(upload_to=user_directory_path, blank=True, null=True)