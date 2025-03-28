from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission

# Create your models here.

class CustomUser(AbstractUser):
	bio = models.TextField()
	profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
	followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)
	groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="customuser_set",
        related_query_name="user",
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="customuser_permissions_set",
        related_query_name="user",
    )

	def __str__(self):
		return self.username