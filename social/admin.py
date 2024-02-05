from django.contrib import admin
from social.models import SocialPost, SocialComment, Image

# Register your models here.
admin.site.register(SocialPost)
admin.site.register(SocialComment)
admin.site.register(Image)