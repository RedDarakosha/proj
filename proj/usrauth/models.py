from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, Group, Permission
from files import models as files

# Create your models here.

class Account(AbstractUser):
	username			=	models.CharField(unique=True, primary_key=True, max_length=64)
#	groups				=	models.ManyToManyField(Group)
#	user_permissions 	=	models.ManyToManyField(Permission)
	slug 				=	models.SlugField(unique=True, blank=True)
	profile 			=	models.ImageField('profile', upload_to='profile_images/', blank=True)
	last_online 		=	models.DateTimeField(default=timezone.now())
	friends 			=	models.ManyToManyField('self', default='')


	images 			=	models.ManyToManyField(files.Image, blank=True, null=True)
	videos 			=	models.ManyToManyField(files.Video, blank=True, null=True)
	music_playlist 	=	models.ManyToManyField(files.Playlist, blank=True, null=True)



	def __str__(self):
		return self.username

	def save(self, *args, **kwargs):
		if self.slug == None:
			self.slug = slugify(self.username)
		return super().save(*args, **kwargs)
