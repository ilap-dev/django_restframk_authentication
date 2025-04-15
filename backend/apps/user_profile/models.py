import uuid
from django.db import models
from ckeditor.fields import RichTextField
from django.conf import settings
from djoser.signals import user_registered, user_activated

User = settings.AUTH_USER_MODEL

# Create your models here.

class UserProfile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #banner_picture = models.ForeignKey()
    birthday = models.DateField(blank=True, null=True)
    biography = RichTextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)


#def post_user_registered(user, *args, **kwargs):
#    print("User has registered")

def post_user_activated(user, *args, **kwargs):
    UserProfile.objects.create(user=user)
    print("User has activated")

#user_registered.connect(post_user_registered)
user_activated.connect(post_user_activated)