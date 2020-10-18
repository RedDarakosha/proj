from django.db import models
from django.utils import timezone
from django.utils.text import slugify
#from usrauth import models as usr
# Create your models here.

class Music(models.Model):
	slug 				=		 models.SlugField(unique=True, blank=True)
	title 				=		 models.CharField(max_length=64, unique=True)
	author	 			=		 models.CharField(max_length=64)
	music 				=		 models.FileField(upload_to='musics/')
	image 				=		 models.ImageField(upload_to='music_images/')
#	users 		=	 models.ManyToManyField(Account)
#	user 		= 	 models.ForeignKey(usr.Account, on_delete=models.CASCADE)

	def save(self, *args, **kwargs):
		if self.slug == None:
			self.slug = slugify(self.title)
		super().save(*args, **kwargs)

	def __str__(self):
		return self.title



class Playlist(models.Model):
	slug 				=		models.SlugField(unique=True, blank=True)
	music 				=		models.ManyToManyField(Music)	
	title 				=		models.CharField(max_length=64,unique=True)
#	users 		=	models.ManyToManyField(Account)
#	user 		= 	models.ForeignKey(usr.Account, on_delete=models.CASCADE)

	def save(self, *args, **kwargs):
		if self.slug == None:
			self.slug = slugify(self.title)
		super().save(*args, **kwargs)


	def __str__(self):
		return self.title


class Video(models.Model):
	slug 				=		 models.SlugField(unique=True, blank=True)
	title		 		=		 models.CharField(max_length=64, default='Noname')
	video 				=		 models.FileField(upload_to='videos/')
#	user 		= 	 models.ForeignKey(usr.Account, on_delete=models.CASCADE)
#	users 		=	 models.ManyToManyField(Account)

	def __str__(self):
		return self.title

	# normal saving with auto generating slug if it does not exist
	def save(self, *args, **kwargs):
		if self.slug == None:
			self.slug = slugify(self.title)
		super().save(*args, **kwargs)


class CommentToVideo(models.Model):
	slug 				=		 models.SlugField(unique=True, blank=True)
	text 				=		 models.TextField()
	likes 				=		 models.PositiveIntegerField(default=0)
	dislikes 			=		 models.PositiveIntegerField(default=0)
	file_first		 	=		 models.FileField(upload_to='comment_to_video/', blank=True, null=True)
	file_second 		=		 models.FileField(upload_to='comment_to_video/', blank=True, null=True)
	file_third 			=		 models.FileField(upload_to='comment_to_video/', blank=True, null=True)	
	file_fourth 		=		 models.FileField(upload_to='comment_to_video/', blank=True, null=True)	
	file_fifth 			=		 models.FileField(upload_to='comment_to_video/', blank=True, null=True)	
	file_sixth			=		 models.FileField(upload_to='comment_to_video/', blank=True, null=True)	
	file_seventh 		=		 models.FileField(upload_to='comment_to_video/', blank=True, null=True)	
	file_eighth 		=		 models.FileField(upload_to='comment_to_video/', blank=True, null=True)	
	file_ninth 			=		 models.FileField(upload_to='comment_to_video/', blank=True, null=True)	

#	user		= 	 models.ForeignKey(usr.Account, on_delete=models.CASCADE)

	def __str__(self):
		return '%s:%s'.format(self.user.username, timezone.now)


	# normal saving with auto generating slug if it does not exist
	def save(self, *args, **kwargs):
		if self.slug == None:
			self.slug = slugify(self.user.username) + " : " + str(timezone.now())
		super().save(*args, **kwargs)


class Image(models.Model):
	slug 				=			 models.SlugField(unique=True, blank=True)
	photo 				=			 models.ImageField(upload_to='images/')
#	user 		=	 models.ForeignKey(usr.Account, on_delete=models.CASCADE)
#	users 		=	 models.ManyToManyField(Account)


	# normal saving with auto generating slug if it does not exist
	def save(self, *args, **kwargs):
		if self.slug == None:
			self.slug = slugify(self.user.username) +" : "+  str(timezone.now())
		super().save(*args, **kwargs)


class CommentToImage(models.Model):
	slug 				=			 models.SlugField(unique=True, blank=True)
	text 				=			 models.TextField()
	likes 				=			 models.PositiveIntegerField(default=0)
	dislikes			=			 models.PositiveIntegerField(default=0)
	file_first 			=			 models.FileField(upload_to='comment_to_image/', blank=True, null=True)
	file_second 		=			 models.FileField(upload_to='comment_to_image/', blank=True, null=True)
	file_third 			=			 models.FileField(upload_to='comment_to_image/', blank=True, null=True)	
	file_fourth 		=			 models.FileField(upload_to='comment_to_image/', blank=True, null=True)	
	file_fifth 			=			 models.FileField(upload_to='comment_to_image/', blank=True, null=True)	
	file_sixth			=			 models.FileField(upload_to='comment_to_image/', blank=True, null=True)	
	file_seventh 		=			 models.FileField(upload_to='comment_to_image/', blank=True, null=True)	
	file_eighth 		=			 models.FileField(upload_to='comment_to_image/', blank=True, null=True)	
	file_ninth 			=			 models.FileField(upload_to='comment_to_image/', blank=True, null=True)	

#	user 		=	 models.ForeignKey(usr.Account, on_delete=models.CASCADE)


	def __str__(self):
		return '%s:%s'.format(self.user.username, timezone.now())

	# normal saving with auto generating slug if it does not exist
	def save(self, *args, **kwargs):
		if self.slug == None:
			self.slug = slugify(self.user.username) + " : "+ str(timezone.now())
		super().save(*args, **kwargs)
